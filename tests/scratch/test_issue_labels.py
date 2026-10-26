import copy
from pathlib import Path

import pytest
from scratch.issue_labels import classify_issue, validate_labels, build_plan, build_index, fingerprint
from scratch.sync_issue_labels import apply_plan


def issue(number=10, title='[監査] 東工大前期1985-3：論証の補修', body='対象：`src/titech/zenki/1985/3/solution.tex`', labels=None):
    return dict(number=number, id=f'I_{number}', title=title, body=body, labels=[{'name': n} for n in (labels or [])], state='CLOSED', url=f'https://github.com/a/b/issues/{number}', updatedAt='2026-10-21T00:00:00Z')


@pytest.fixture
def root(tmp_path):
    p=tmp_path/'src/titech/zenki/1985/3';p.mkdir(parents=True);(p/'solution.tex').write_text('source')
    return tmp_path


def test_closed_single_question_and_kinds(root):
    r=classify_issue(issue(labels=['bug']), root)
    assert r['status']=='candidate'
    assert r['problem_id']=='titech/zenki/1985/3'
    assert set(r['labels'])=={'problem:titech/zenki/1985/3','univ:titech','exam:zenki','year:1985','kind:proof'}


@pytest.mark.parametrize('title,body', [
    ('[fix/converter] 表示修正 (titech zenki 1985-3)', 'src/titech/zenki/1985/3/solution.tex'),
    ('caption不足のまとめ', 'src/titech/zenki/1985/3/solution.tex'),
    ('東工大前期1985年 全体サマリ', ''),
])
def test_global_issues_never_use_example_paths(root,title,body):
    assert classify_issue(issue(title=title,body=body),root)['status']=='excluded'


def test_conflicting_paths_labels_and_missing_source_need_review(root):
    for i in [issue(body='src/titech/zenki/1985/3/solution.tex src/utokyo/zenki/1985/3/solution.tex'),issue(labels=['univ:utokyo']),issue(title='[TeX化] 東工大前期1999年 第3問',body='')]:
        assert classify_issue(i,root)['status']=='review'


def test_marker_and_english_title(root):
    i=issue(title='titech/zenki 1985/3: TikZコンパイル失敗',body='<!-- solution-figure-loss:titech/zenki/1985/3 -->')
    r=classify_issue(i,root)
    assert r['status']=='candidate' and 'kind:figure' in r['labels']


def test_label_validation_and_index_do_not_guess_from_title():
    valid=['problem:titech/zenki/1985/3','univ:titech','exam:zenki','year:1985','kind:proof']
    assert validate_labels(valid)==('titech/zenki/1985/3',None)
    for names in [valid+['univ:utokyo'],valid+['problem:utokyo/zenki/1985/3'],valid[:-2],valid+['kind:unknown']]:
        assert validate_labels(names)[1]
    data=build_index([issue(labels=valid),issue(number=11)],'a/b')
    assert len(data['problems']['titech/zenki/1985/3'])==1
    assert data['problems']['titech/zenki/1985/3'][0]['state']=='closed'


def test_override_requires_matching_fingerprint_and_reason(root):
    i=issue(body='src/titech/zenki/1985/3/solution.tex src/utokyo/zenki/1985/3/solution.tex')
    override={str(i['number']):dict(problem_id='titech/zenki/1985/3',reason='Reviewed comparison path',fingerprint=fingerprint(i))}
    assert classify_issue(i,root,override)['status']=='candidate'
    i['body']+=' edited'
    assert classify_issue(i,root,override)['status']=='review'


class FakeClient:
    def __init__(self, issues):self.issues=copy.deepcopy(issues);self.created=[];self.added=[]
    def fetch(self,numbers=None):return [i for i in self.issues if numbers is None or i['number'] in numbers]
    def ensure_labels(self,names):self.created.extend(names);return {n:n for n in names}
    def add_labels(self,updates):
        self.added.extend(updates)
        for ident,names in updates:
            i=next(i for i in self.issues if i['id']==ident)
            i['labels'] += [{'name':n} for n in names if n not in {x['name'] for x in i['labels']}]


def test_apply_adds_only_and_is_idempotent(root):
    i=issue(labels=['bug']);client=FakeClient([i]);plan=build_plan([i],root,'a/b')
    result=apply_plan(plan,client,root)
    assert result['applied']==[10]
    assert client.issues[0]['body']==i['body'] and client.issues[0]['state']=='CLOSED'
    assert 'bug' in {x['name'] for x in client.issues[0]['labels']}
    plan2=build_plan(client.fetch(),root,'a/b');client.created=[];client.added=[]
    assert apply_plan(plan2,client,root)['applied']==[]
    assert not client.created and not client.added


def test_stale_plan_and_tampered_plan_do_not_write(root):
    i=issue();plan=build_plan([i],root,'a/b');client=FakeClient([i]);client.issues[0]['title']+=' changed'
    assert apply_plan(plan,client,root)['skipped']
    assert not client.created and not client.added
    client=FakeClient([i]);plan['issues'][0]['labels'].append('univ:utokyo')
    assert apply_plan(plan,client,root)['skipped']
    assert not client.created and not client.added


def test_issue_edited_during_label_creation_is_not_written(root):
    i=issue();plan=build_plan([i],root,'a/b')
    class EditedClient(FakeClient):
        def ensure_labels(self,names):
            self.issues[0]['body']+=' concurrent edit'
            return super().ensure_labels(names)
    client=EditedClient([i])
    result=apply_plan(plan,client,root)
    assert not client.added and result['skipped']


def test_partial_failure_is_recorded_and_propagated(root):
    i=issue();plan=build_plan([i],root,'a/b');progress=[]
    class FailedClient(FakeClient):
        def add_labels(self,updates):raise RuntimeError('rate limit or partial write')
    with pytest.raises(RuntimeError):apply_plan(plan,FailedClient([i]),root,lambda r:progress.append(copy.deepcopy(r)))
    assert progress[-1]['error']=='rate limit or partial write'


def test_cli_default_is_offline_plan_only(root,tmp_path):
    import json
    from scratch.sync_issue_labels import main
    snapshot=tmp_path/'issues.json';snapshot.write_text(json.dumps([issue()]))
    output=tmp_path/'plan.json'
    with __import__('unittest.mock',fromlist=['patch']).patch('scratch.sync_issue_labels.GitHub.gh',side_effect=AssertionError('network write/read forbidden')):
        assert main(['--issues-json',str(snapshot),'--root',str(root),'--plan',str(output)])==0
    assert json.loads(output.read_text())['summary']=={'candidate':1}

@pytest.mark.parametrize('title,body', [
    ('東工大前期1985-3・4の論証を修正', ''),
    ('東工大前期1985-3の論証', '東工大前期1985年 第4問も同じIssueで修正する。'),
])
def test_multiple_questions_in_prose_are_reviewed(root, title, body):
    assert classify_issue(issue(title=title, body=body), root)['status'] == 'review'


def test_single_question_web_display_is_eligible(root):
    assert classify_issue(issue(title='[Web表示] 東工大前期1985-3 図の欠落'), root)['status'] == 'candidate'


def test_stale_labels_on_aggregate_are_rejected():
    labels=['problem:titech/zenki/1985/3','univ:titech','exam:zenki','year:1985']
    result=build_index([issue(title='全サイトのまとめ',labels=labels)])
    assert not result['problems'] and result['rejected']


def test_graphql_payloads_use_variables_and_preserve_label_lists():
    from scratch.sync_issue_labels import GitHub
    class RecordingGitHub(GitHub):
        def __init__(self):
            super().__init__('a/b', interval=0)
            self.calls=[]
        def gh(self,args,payload=None):
            self.calls.append((args,payload))
            query=payload['query']
            if query.startswith('mutation'):
                return {'data':{'i0':{'clientMutationId':None}}}
            return {'data':{'repository':{'i0':dict(issue(),labels={'totalCount':1,'nodes':[{'name':'bug'}]})}}}
    client=RecordingGitHub()
    assert client.fetch([10])[0]['labels']==[{'name':'bug'}]
    client.add_labels([('I_10',['L_1'])])
    query=client.calls[-1][1]
    assert query['variables']=={'issue0':'I_10','labels0':['L_1']}
    assert 'I_10' not in query['query'] and 'L_1' not in query['query']


def test_concurrent_conflicting_label_is_skipped(root):
    i=issue();plan=build_plan([i],root,'a/b')
    class ConflictingClient(FakeClient):
        def ensure_labels(self,names):
            self.issues[0]['labels'].append({'name':'univ:utokyo'})
            return super().ensure_labels(names)
    client=ConflictingClient([i])
    assert apply_plan(plan,client,root)['skipped'] and not client.added


def test_stale_labels_on_multiple_questions_are_rejected():
    labels=['problem:titech/zenki/1985/3','univ:titech','exam:zenki','year:1985']
    for i in [issue(title='東工大前期1985-3・4の論証を修正',labels=labels),
              issue(body='東工大前期1985年 第4問も対象',labels=labels)]:
        result=build_index([i])
        assert not result['problems'] and result['rejected']


def test_report_year_range_does_not_count_as_another_question():
    labels=['problem:ukyoto/kouki/1999/5','univ:ukyoto','exam:kouki','year:1999']
    i=issue(title='[監査] 京大後期1999年第5問',
            body='`src/ukyoto/kouki/1999/5/solution.tex` and '
                 '`docs/audit/reports/2026-10-25-ukyoto-kouki-1998-2000/diagnostic/1999-5.pdf`',
            labels=labels)
    result=build_index([i])
    assert not result['rejected']
    assert len(result['problems']['ukyoto/kouki/1999/5'])==1


def test_initial_fetch_failure_is_recorded(root):
    plan=build_plan([issue()],root,'a/b');progress=[]
    class FailedReadClient(FakeClient):
        def fetch(self,numbers=None):raise RuntimeError('HTTP 502 on refresh')
    with pytest.raises(RuntimeError):
        apply_plan(plan,FailedReadClient([]),root,lambda r:progress.append(copy.deepcopy(r)))
    assert progress[-1]['error']=='HTTP 502 on refresh'

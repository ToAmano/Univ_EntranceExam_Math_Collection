#!/usr/bin/env python3
"""Plan/add single-question labels via gh; dry-run by default. See docs/issue-labels.md."""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

if __package__:
    from .issue_labels import DEFAULT_REPO, build_index, build_plan, classify_issue, fingerprint, names
else:
    from issue_labels import DEFAULT_REPO, build_index, build_plan, classify_issue, fingerprint, names

ROOT = Path(__file__).resolve().parent.parent
FIELDS = 'number,id,title,body,state,labels,url,updatedAt'
BATCH_SIZE = 20


def chunks(items, size=BATCH_SIZE):
    for start in range(0, len(items), size):
        yield items[start:start + size]


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


class GitHub:
    def __init__(self, repo, interval=4):
        self.repo, self.interval = repo, interval
        self.last_write = 0

    def gh(self, args, payload=None):
        result = subprocess.run(['gh', *args], input=json.dumps(payload) if payload is not None else None,
                                text=True, capture_output=True)
        if result.returncode:
            raise RuntimeError(result.stderr.strip() or 'gh request failed')
        return json.loads(result.stdout)

    def graphql(self, query, variables, mutation=False):
        if mutation:
            remaining = self.interval - (time.monotonic() - self.last_write)
            if remaining > 0:
                time.sleep(remaining)
            self.last_write = time.monotonic()
        data = self.gh(['api', 'graphql', '--input', '-'], {'query': query, 'variables': variables})
        if data.get('errors'):
            # GraphQL can partially succeed. Stop; a fresh plan/retry discovers
            # already-created labels and additions without overwriting anything.
            raise RuntimeError('GraphQL errors (may be partial): ' + json.dumps(data['errors']))
        return data['data']

    def fetch(self, numbers=None):
        if numbers is not None:
            owner, repo = self.repo.split('/')
            issues = []
            for batch in chunks(list(numbers)):
                declarations = ['$owner:String!', '$repo:String!']
                variables = dict(owner=owner, repo=repo)
                fields = []
                for n, number in enumerate(batch):
                    declarations.append(f'$n{n}:Int!')
                    variables[f'n{n}'] = number
                    fields.append(f'i{n}:issue(number:$n{n}){{number id title body state url updatedAt labels(first:100){{totalCount nodes{{name}}}}}}')
                data = self.graphql('query(' + ','.join(declarations) + '){repository(owner:$owner,name:$repo){' + ' '.join(fields) + '}}', variables)
                for issue in data['repository'].values():
                    if issue is None:
                        continue
                    if issue['labels']['totalCount'] > 100:
                        raise RuntimeError('Issue label pagination required')
                    issue['labels'] = issue['labels']['nodes']
                    issues.append(issue)
            return issues
        issues = self.gh(['issue', 'list', '-R', self.repo, '--state', 'all', '--limit', '10000', '--json', FIELDS])
        if len(issues) == 10000:
            raise RuntimeError('Issue fetch limit reached; use pagination before proceeding')
        return issues if numbers is None else [i for i in issues if i['number'] in numbers]

    def ensure_labels(self, required):
        owner, repo = self.repo.split('/')
        data = self.graphql('query($owner:String!,$repo:String!){repository(owner:$owner,name:$repo){id}}', {'owner': owner, 'repo': repo})
        repository_id = data['repository']['id']
        pages = self.gh(['api', '--paginate', '--slurp', f'repos/{self.repo}/labels?per_page=100'])
        ids = {label['name']: label['node_id'] for page in pages for label in page}
        missing = sorted(set(required) - ids.keys())
        for batch in chunks(missing):
            declarations, fields, variables = ['$repository:ID!'], [], {'repository': repository_id}
            for i, name in enumerate(batch):
                declarations += [f'$name{i}:String!', f'$color{i}:String!', f'$description{i}:String!']
                prefix = name.split(':', 1)[0]
                variables.update({f'name{i}': name, f'color{i}': {'problem': '1d76db', 'univ': '5319e7', 'exam': '0052cc', 'year': 'c5def5', 'kind': 'd4c5f9'}[prefix], f'description{i}': f'Issue label convention: {name}'})
                fields.append(f'l{i}:createLabel(input:{{repositoryId:$repository,name:$name{i},color:$color{i},description:$description{i}}}){{label{{id name}}}}')
            data = self.graphql('mutation(' + ','.join(declarations) + '){' + ' '.join(fields) + '}', variables, mutation=True)
            for value in data.values():
                label = value['label']
                ids[label['name']] = label['id']
            print(f'Created {len(batch)} labels', flush=True)
        return {name: ids[name] for name in required}

    def add_labels(self, updates):
        declarations, fields, variables = [], [], {}
        for i, (ident, label_ids) in enumerate(updates):
            declarations += [f'$issue{i}:ID!', f'$labels{i}:[ID!]!']
            variables.update({f'issue{i}': ident, f'labels{i}': label_ids})
            fields.append(f'i{i}:addLabelsToLabelable(input:{{labelableId:$issue{i},labelIds:$labels{i}}}){{clientMutationId}}')
        self.graphql('mutation(' + ','.join(declarations) + '){' + ' '.join(fields) + '}', variables, mutation=True)


def apply_plan(plan, client, root=ROOT, progress=None):
    if plan.get('schema_version') != 1:
        raise ValueError('Unsupported plan version')
    selected = [r for r in plan['issues'] if r['status'] == 'candidate']
    result = dict(repo=plan['repo'], applied=[], unchanged=[], skipped=[], error=None)
    if not selected:
        return result
    if progress:
        progress(result)
    print(f'Refreshing {len(selected)} issues', flush=True)
    try:
        current = {i['number']: i for i in client.fetch([r['number'] for r in selected])}
    except Exception as error:
        result['error'] = str(error)
        if progress:
            progress(result)
        raise
    pending = []
    for row in selected:
        issue = current.get(row['number'])
        reason = None
        if not issue or fingerprint(issue) != row['fingerprint'] or issue.get('id') != row['id']:
            reason = 'issue changed or disappeared since plan'
        else:
            fresh = classify_issue(issue, root, plan.get('overrides'))
            if fresh['status'] != 'candidate' or fresh['problem_id'] != row['problem_id'] or fresh['labels'] != row['labels']:
                reason = 'plan no longer agrees with convention or current issue'
        if reason:
            result['skipped'].append(dict(number=row['number'], reason=reason))
            continue
        additions = sorted(set(row['labels']) - names(issue))
        if additions:
            pending.append((issue, additions))
        else:
            result['unchanged'].append(row['number'])
    if progress:
        progress(result)
    try:
        if pending:
            print('Resolving required labels', flush=True)
            ids = client.ensure_labels({n for _, labels in pending for n in labels})
            rows = {r['number']: r for r in selected}
            for batch in chunks(pending, size=5):
                print(f'Refreshing batch starting at #{batch[0][0]["number"]}', flush=True)
                refreshed = {i['number']: i for i in client.fetch([i['number'] for i, _ in batch])}
                updates, applied = [], []
                for old, _ in batch:
                    row = rows[old['number']]
                    issue = refreshed.get(old['number'])
                    fresh = classify_issue(issue, root, plan.get('overrides')) if issue else None
                    if (not issue or fingerprint(issue) != row['fingerprint'] or issue.get('id') != row['id']
                            or fresh['status'] != 'candidate' or fresh['problem_id'] != row['problem_id']
                            or fresh['labels'] != row['labels']):
                        result['skipped'].append(dict(number=row['number'], reason='issue changed before batch write'))
                        continue
                    additions = sorted(set(row['labels']) - names(issue))
                    if additions:
                        updates.append((issue['id'], [ids[n] for n in additions]))
                        applied.append(issue['number'])
                    else:
                        result['unchanged'].append(issue['number'])
                if updates:
                    client.add_labels(updates)
                    result['applied'].extend(applied)
                if progress:
                    progress(result)
                print(f'Labelled {len(result["applied"])}/{len(pending)} issues', flush=True)
    except Exception as error:
        result['error'] = str(error)
        if progress:
            progress(result)
        raise
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', default=DEFAULT_REPO)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--issue', type=int)
    parser.add_argument('--issues-json', type=Path, help='Offline gh issue-list snapshot (read-only modes only)')
    parser.add_argument('--overrides', type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--apply-plan', type=Path)
    mode.add_argument('--export', type=Path)
    parser.add_argument('--plan', type=Path, default=Path('issue-label-plan.json'))
    parser.add_argument('--report', type=Path, default=Path('issue-label-result.json'))
    args = parser.parse_args(argv)
    client = GitHub(args.repo)
    if args.apply_plan:
        if args.issues_json or args.overrides or args.issue:
            parser.error('apply uses the saved plan and fresh GitHub data; no input overrides allowed')
        plan = json.loads(args.apply_plan.read_text(encoding='utf-8'))
        if plan['repo'] != args.repo:
            parser.error('plan repository differs from --repo')
        result = apply_plan(plan, client, args.root, lambda data: write_json(args.report, data))
        write_json(args.report, result)
        print(json.dumps(result, ensure_ascii=False))
        return 1 if result['skipped'] else 0
    issues = json.loads(args.issues_json.read_text(encoding='utf-8')) if args.issues_json else client.fetch([args.issue] if args.issue else None)
    if args.issue:
        issues = [i for i in issues if i['number'] == args.issue]
    if args.export:
        data = build_index(issues, args.repo)
        write_json(args.export, data)
        print(f'Exported {len(data["problems"])} problems; rejected {len(data["rejected"])} issues')
        return 1 if data['rejected'] else 0
    overrides = json.loads(args.overrides.read_text(encoding='utf-8')) if args.overrides else {}
    plan = build_plan(issues, args.root, args.repo, overrides)
    write_json(args.plan, plan)
    print(json.dumps(plan['summary'], ensure_ascii=False))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (RuntimeError, ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)

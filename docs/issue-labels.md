# 一問単位のIssueラベル規約

2026-10-21作成。対象は一問に対応するIssueのみ。GitHubでの絞り込みと、将来のWebページへの関連Issue表示に同じ問題IDを使う。

この文書はラベル規約，同期ツール，Webページへの表示を定める。

## 対象

大学・日程・年度・大問番号を一意に特定でき、内容がその一問に限定されているIssueを対象とする。open/closedを問わず、解決済みの履歴も対象に含める。

次は対象外とし、この規約のラベルを付けない。

- 複数問題のまとめIssue（例：#592、#595）。含まれる問題を個別に抽出してラベル付け・Web連携する作業も、今回は行わない。
- サイト・変換処理・CI全体のIssue（例：#7、#510、#752）。本文に問題例が出ていても、それを対象問題とみなさない。
- 年度全体の完成管理やサマリ（問題番号0）、一問に確定できないIssue。

同じ一問の問題文・解答・図表・Web表示は、同じ問題IDを使う。小問ごとのIDは作らない。複数問題を扱うようになったIssueは、この規約の対象から外して人が整理する。

## 問題IDと必須ラベル

問題IDは `src/{大学}/{日程}/{年度}/{大問番号}/` に対応する次の文字列とする。

```text
titech/zenki/1985/3
```

対象Issueには次の4ラベルを各1個付ける。問題IDラベルを識別の正本とし、残り3個は問題IDから導出する検索用の属性とする。

| ラベル | 例 | ルール |
|---|---|---|
| `problem:{問題ID}` | `problem:titech/zenki/1985/3` | 大学・日程・年度・大問番号を一意に識別 |
| `univ:{大学}` | `univ:titech` | `utokyo` / `ukyoto` / `titech` |
| `exam:{日程}` | `exam:zenki` | `zenki` / `kouki` |
| `year:{年度}` | `year:1985` | 西暦4桁 |

大学・日程は小文字ASCIIのリポジトリ表記を使う。日本語名や旧称・新称による別ラベルは作らない。年度は入試年度を使い、Issue作成年度は使わない。大問番号は正の整数で、ゼロ埋めしない。`sample_`、ファイル名、拡張子、`problem` / `solution` の別は問題IDに含めない。

問題IDラベルの形式は次の正規表現に従う。

```regex
^problem:(utokyo|ukyoto|titech)/(zenki|kouki)/[0-9]{4}/[1-9][0-9]*$
```

形式一致だけでは付与しない。正式な収録先と照合し、重複収録・番号の振替・参照資料のパス等と区別する。例：後期の問題が前期の7〜9番へ重複収録されていたケースは、自動で別問題として扱わない。

問題ファイルが未作成でも、出典から正式な問題と収録予定先を確定できれば対象にできる。ファイルの存在だけでは判定しない。

ラベル例：

```text
problem:titech/zenki/1985/3
univ:titech
exam:zenki
year:1985
```

## 指摘内容のラベル

内容を確認できる場合、次の `kind:*` を1個以上付ける。同じ一問に複数種類の指摘があれば併用する。

| ラベル | 対象 |
|---|---|
| `kind:proof` | 数式・論証・最終答案・数学的な記述の誤りや検証 |
| `kind:figure` | 図表の欠落、TikZ、caption、配置、視認性、図表の生成・表示 |
| `kind:reference` | 式・図・表の番号、label、cref、参照リンク |
| `kind:transcription` | 元原稿との照合、文字起こしの誤記・欠落、未収録 |
| `kind:style` | 句読点、字下げ、フォントなど、上記に含まれない書式 |

図表のcaption不足は `kind:figure`、参照先が壊れている問題は `kind:reference` とする。図表の数学的内容も誤っていれば `kind:proof` を併用する。誤記の発生源が不明な数学的指摘に、推測だけで `kind:transcription` は付けない。

`bug`、`enhancement` など既存ラベルは別の分類軸として保持する。この規約の導入時に削除・置換しない。open/closedや人による確認状況を `kind:*` で表現しない。

既存Issueの移行時、問題は特定できても指摘の分類が曖昧なら、4つの識別ラベルだけを付与候補にし、`kind:*` は要確認として残す。

## GitHubでの検索・並べ替え

リポジトリのIssues画面では、例えば次のように検索する。

```text
is:issue is:open label:"problem:titech/zenki/1985/3"
is:issue label:"problem:titech/zenki/1985/3"
is:issue is:open label:"univ:titech" label:"exam:zenki" label:"year:1985"
is:issue is:open label:"univ:titech" label:"kind:proof" sort:updated-desc
```

2行目は解決済みの履歴も含む。一意の問題IDを使うので、タイトルの表記や変更に検索が依存しない。

ラベルは絞り込みに使う。年度・問題番号を数値として順に並べ替える機能はこの規約に含めず、必要になった段階でGitHub Projectsのフィールド等を検討する。

## 既存Issueへの適用手順

1. 対象候補を読み取り専用で一覧化する。問題ID、根拠となるタイトル・本文のパス・既存の識別コメント、付与予定ラベルを示す。
2. 一問に確定できるものと、対象外・要確認のものを区別する。タイトルと本文、複数のパスが食い違うものは自動確定しない。
3. 確定した対象に、必要なラベルを作成・付与する。Issueが存在しない全問題分のラベルは先に大量作成しない。
4. 必須4ラベルの整合と、既存ラベルが保持されていることを確認する。

既存の識別コメント（例：`<!-- math-audit-question:titech/zenki/1981/4 -->`）やソースパスは照合の根拠として使い、ラベルと矛盾する場合は要確認とする。例示・比較対象・リンク先に登場しただけの問題は紐付けない。

ラベル付与だけでIssueをclose/reopenしたり、数学的な指摘を採用・棄却したりしない。原稿、タイトル、本文、commitとの対応も変更しない。同一問題のIssueが複数存在しても、この作業を理由に自動統合・削除せず、同じ問題IDで取得できるようにする。新規指摘は既存の一問Issueへの追記を基本とする。

## 将来の自動付与・Web連携との境界

新規Issueは、対象を明記する入力から問題IDを確定し、4ラベルと内容分類を付ける。Webの報告フォームから作成する場合も、ページの大学・日程・年度・大問番号から同じIDを作る。ラベルが利用者側で設定されなかった場合も考慮し、作成後の同期処理で検証する設計とする。

Web側は `problem:*` を持ち、必須4ラベルが整合するIssueだけをその一問へ紐付ける。対象外のまとめIssueや全体Issueは取り込まない。タイトル・本文の推測検索はWebでの恒常的な紐付けには使わない。

一問から複数Issueを取得できる対応表とし、GitHubのopen/closed状態、タイトル、URL、更新日時を保持する。問題文・解答の両ページから同じ対応表を参照する。通常のサイトビルド時に取得し、検証済みJSONを使ってOpenなIssueだけを問題文・解答ページに表示する。

矛盾した問題IDや複数の `problem:*` を持つIssueは、一問への表示から除外して要確認として報告する。ラベル名や正式な収録先を変更する場合は、検索用属性・既存Issue・Web対応表を併せて移行する。

## 付与時の整合条件

- 対象Issueの `problem:*` はちょうど1個。
- `univ:*` / `exam:*` / `year:*` も各1個で、問題IDから導出した値と一致する。
- 正式な対象問題が確認でき、Issueの内容もその一問だけに対応する。
- `kind:*` は上記の定義済み値を使う。未確定の分類は推測で埋めない。
- open/closedの変更、人による確認完了の判定、原稿の修正はラベル同期では行わない。

## 同期CLIとActions

Python 3.9以上と認証済みの `gh` を使う。追加のPythonライブラリは不要。

```sh
# 読み取り専用。closedも含む全Issueの計画を作る
python scratch/sync_issue_labels.py --plan issue-label-plan.json
# 単一Issueに限定する場合
python scratch/sync_issue_labels.py --issue 600 --plan issue-label-plan.json
# 保存済み計画を再検証して適用（既存ラベルへの追加のみ）
python scratch/sync_issue_labels.py --apply-plan issue-label-plan.json --report issue-label-result.json
# 検証済みラベルからWeb連携用JSONを出力
python scratch/sync_issue_labels.py --export issues-by-problem.json
```

`--issues-json` で `gh issue list --state all --json number,id,title,body,state,labels,url,updatedAt` 形式のスナップショットを読み込み、オフラインで計画・対応表を出せる。適用時には使用できない。

判定はタイトル・識別コメント・本文の問題パス・既存ラベルを照合し、正式なソースがある一問だけを候補にする。タイトルや識別コメントに対象がない一般Issueは本文の例だけで推定しない。既存ラベルに矛盾があれば変更しない。指摘分類が確定しないものは `kind_review: true` として識別ラベルだけを候補にする。

手動確認した例外は `--overrides overrides.json` で計画に取り込める。キーはIssue番号の文字列、値は `problem_id`、確認理由 `reason`、計画の `fingerprint`、任意の `kinds`（`proof` 等の配列）。本文・タイトルが変わると例外は無効になる。

付与は5件単位、API書き込みの開始間隔は最低4秒とする（取得・ラベル作成は20件単位）。適用時は計画の問題ID・予定ラベルを再計算し、各書き込みバッチ直前にもIssueを再取得する。API失敗時は停止し、途中結果を保存する。GraphQLは部分成功しうるため、再取得して新しい計画を作ってから再実行する。既に付いたラベルは再追加しない。最後の再取得とAPI書き込みの間の編集をGitHub側で原子的に排除する機能はない。

対応表は `schema_version`, `repo`, `generated_at`, `problems`, `rejected` を持つ。`problems` は問題IDをキーとし、Issueの `number`, `title`, `state`, `url`, `updated_at`, `kinds` の配列を返す。未ラベルIssueは取り込まず、識別ラベルが不整合なものや、現在の記述がまとめ・全体・複数問題を示すものは `rejected` に理由を残す。ラベルの削除は自動実行しない。

`.github/workflows/issue-labels.yml` はIssueの作成・編集時にその一件を同期する。手動実行は既定でdry-run。`apply` を選ぶと適用する。計画と結果はartifactに残り、review/excludedは変更しない。このworkflowはデフォルトブランチへの反映後に有効になる。


## Webページでの表示

問題文・解答ページは同じ問題IDでOpenなIssueを表示する。タイトル・番号からGitHubへ移動でき、取得日時と該当ラベルのOpen Issue検索リンクも付ける。0番の年度サマリには表示しない。Open Issueが0件でも、原稿の完全性や全指摘の解消を保証する表示ではなく、紐付けられたIssueがないことを示す。

ローカルではWebビルド前に対応表を生成する。

```sh
python scratch/sync_issue_labels.py --export web/src/data/issues-by-problem.json
cd web
npm test
NODE_OPTIONS=--max-old-space-size=6144 npm run build
```

生成JSONはgit管理対象外。オフライン確認では以前のexport結果を同じ場所へコピーして利用できる。取得を省略した `npm run build` はネットワークアクセスせず既存JSONを使う。データが未取得・壊れている場合は「取得できていません」とGitHub検索リンクを表示し、0件とは扱わない。

Pagesの既存のpush/main・手動ビルドでは、読み取り専用のGitHub API取得を一度追加した。ラベル不整合でexportが失敗した場合は公開処理を停止する。ページごとのAPI呼び出しや閲覧者側の認証は不要。Issueの作成・編集・closeを理由にしたサイトビルドは追加していないため、公開表示は次の通常ビルドまで古いことがある。最新状態は各ページのGitHub検索リンクから確認できる。

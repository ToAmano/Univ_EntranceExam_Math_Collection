#!/usr/bin/env python3
"""data/problem_groups.yaml（#1411 類題カタログ）の整合性を検査する。

検査内容:
  - 各グループに id・name・problems・related があること
  - id が重複していないこと
  - 問題ID が src/<大学>/<日程>/<年>/<大問番号>/problem.tex に実在すること
  - 1つのグループ内で同じ問題が重複していないこと（problems と related の重複も含む）

使い方:
    python3 scratch/check_problem_groups.py [data/problem_groups.yaml]

問題があれば一覧を表示して終了コード 1 を返す。
"""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PATH = ROOT / "data" / "problem_groups.yaml"
REQUIRED_KEYS = ("id", "name", "problems", "related")


def check(path: Path) -> list[str]:
    errors: list[str] = []
    groups = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not isinstance(groups, list):
        return [f"{path}: 最上位はグループのリストである必要があります"]

    seen_ids: set[str] = set()
    for index, group in enumerate(groups):
        label = group.get("id", f"#{index}") if isinstance(group, dict) else f"#{index}"
        if not isinstance(group, dict):
            errors.append(f"{label}: グループは辞書である必要があります")
            continue
        for key in REQUIRED_KEYS:
            if key not in group:
                errors.append(f"{label}: '{key}' がありません")
        gid = group.get("id")
        if gid in seen_ids:
            errors.append(f"{label}: id が重複しています")
        seen_ids.add(gid)

        members = [*(group.get("problems") or []), *(group.get("related") or [])]
        if not group.get("problems"):
            errors.append(f"{label}: problems が空です")
        duplicates = sorted({m for m in members if members.count(m) > 1})
        for dup in duplicates:
            errors.append(f"{label}: {dup} がグループ内で重複しています")
        for member in members:
            if not (ROOT / "src" / member / "problem.tex").is_file():
                errors.append(f"{label}: {member} に対応する src/{member}/problem.tex がありません")
    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    errors = check(path)
    groups = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if errors:
        print(f"[FAIL] {path}（{len(errors)} 件）")
        for error in errors:
            print(f"  - {error}")
        return 1
    count = sum(len(g.get("problems") or []) + len(g.get("related") or []) for g in groups)
    print(f"[PASS] {path}: {len(groups)} グループ・延べ {count} 問")
    return 0


if __name__ == "__main__":
    sys.exit(main())

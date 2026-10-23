"""Report the GitHub Pages artifact size and flag growth near its limit."""

import argparse
import os
from pathlib import Path


def check_size(directory: Path, warning_bytes: int, limit_bytes: int) -> int:
    total = sum(path.stat().st_size for path in directory.rglob('*') if path.is_file())
    print(f'Pages artifact: {total:,} bytes ({total / 1_000_000:.1f} MB)')
    if total > limit_bytes:
        print(f'::error::Pages artifact exceeds {limit_bytes / 1_000_000:.0f} MB limit')
        return 1
    if total > warning_bytes:
        prefix = '::warning::' if os.getenv('GITHUB_ACTIONS') else 'WARNING: '
        print(f'{prefix}Pages artifact exceeds {warning_bytes / 1_000_000:.0f} MB warning threshold')
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--warning-mb', type=int, default=900)
    parser.add_argument('--limit-mb', type=int, default=1000)
    args = parser.parse_args()
    if not args.directory.is_dir():
        parser.error(f'not a directory: {args.directory}')
    raise SystemExit(check_size(args.directory, args.warning_mb * 1_000_000, args.limit_mb * 1_000_000))


if __name__ == '__main__':
    main()

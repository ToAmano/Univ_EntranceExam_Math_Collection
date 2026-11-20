#!/usr/bin/env python3
"""Compare figure-audit reports against reviewed, hash-pinned examples."""

import argparse
import json
from pathlib import Path


def evaluate(cases, reports):
    by_hash = {report['source_sha256']: report for report in reports}
    if len(by_hash) != len(reports):
        raise ValueError('duplicate report source hashes')
    total = detected = reviewed_nonactionable = 0
    case_results = []
    for case in cases:
        report = by_hash.get(case['sha256'])
        if report is None:
            raise ValueError(f"no report with pinned hash for Issue #{case['issue']}")
        figures = {figure['figure_index']: figure for figure in report['figures']}
        hits = []
        for expected in case['expected_pairs']:
            total += 1
            figure = figures.get(expected['figure_index'])
            found = bool(figure and figure['status'] == 'ready' and any(
                set(expected['nodes']) == {candidate['a'], candidate['b']}
                for candidate in figure['candidates']))
            detected += found
            hits.append({'figure_index': expected['figure_index'],
                         'nodes': expected['nodes'], 'detected': found})
        for reviewed in case.get('reviewed_nonactionable_pairs', []):
            figure = figures.get(reviewed['figure_index'])
            if not figure or not any(
                set(reviewed['nodes']) == {candidate['a'], candidate['b']}
                for candidate in figure['candidates']
            ):
                raise ValueError(f"reviewed pair missing for Issue #{case['issue']}")
            reviewed_nonactionable += 1
        case_results.append({'issue': case['issue'], 'expected_pairs': hits,
                             'figures': len(figures),
                             'candidates': sum(len(f['candidates']) for f in figures.values()),
                             'reviewed_nonactionable_pairs': len(case.get('reviewed_nonactionable_pairs', [])),
                             'unavailable': sum(f['status'] != 'ready' for f in figures.values())})
    return {'detected_pairs': detected, 'expected_pairs': total,
            'reviewed_nonactionable_pairs': reviewed_nonactionable,
            'cases': case_results,
            'note': 'Small reviewed sample; not a general recall or false-positive estimate.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cases', type=Path, default=Path(__file__).with_name('figure_cases.json'))
    parser.add_argument('--report', type=Path, action='append', required=True)
    args = parser.parse_args()
    cases = json.loads(args.cases.read_text(encoding='utf-8'))['cases']
    reports = [json.loads(path.read_text(encoding='utf-8')) for path in args.report]
    print(json.dumps(evaluate(cases, reports), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

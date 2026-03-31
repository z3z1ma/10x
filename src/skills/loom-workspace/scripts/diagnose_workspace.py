#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(SCRIPT_DIR.parent))

from _loom_lib.core import doctor_report, find_workspace_root  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Loom workspace health")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    workspace = find_workspace_root()
    report = doctor_report(workspace)
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(f"workspace: {report['workspace']}")
        print(f"bundle_layout: {report['bundle_layout']}")
        print(f"rules_root: {report['rules_root']}")
        print(f"skills_root: {report['skills_root']}")
        print(f"healthy: {report['healthy']}")
        print(f"skill_count: {report['skill_count']}")
        print(f"record_issue_count: {report['record_issue_count']}")
        print(f"link_issue_count: {report['link_issue_count']}")
        if report["missing_directories"]:
            print("missing_directories:")
            for item in report["missing_directories"]:
                print(f"  - {item}")
        if report["skill_issues"]:
            print("skill_issues:")
            for item in report["skill_issues"]:
                print(f"  - {item}")
    return 1 if not report["healthy"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

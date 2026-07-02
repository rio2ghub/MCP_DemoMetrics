#!/usr/bin/env python
"""Code Review Agent CLI - Run code reviews before pushing to GitHub."""

import sys
import json
import logging
from pathlib import Path
from typing import List

from src.code_review_agent import CodeReviewAgent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def print_report(summary: dict) -> None:
    """Print formatted code review report.

    Args:
        summary: Review summary dictionary
    """
    print("\n" + "=" * 70)
    print("CODE REVIEW REPORT")
    print("=" * 70)

    print(f"\nTotal Files Reviewed: {summary['total_files']}")
    print(f"✓ Passed: {summary['passed']}")
    print(f"⚠ Warnings: {summary['warnings']}")
    print(f"✗ Failed: {summary['failed']}")
    print(f"\nTotal Issues Found: {summary['total_issues']}")
    print(f"Total Warnings: {summary['total_warnings']}")

    # Print details for each file
    if summary["files"]:
        print("\n" + "-" * 70)
        print("FILE DETAILS")
        print("-" * 70)

        for report in summary["files"]:
            status_icon = (
                "✓"
                if report["status"] == "passed"
                else "⚠"
                if report["status"] == "warning"
                else "✗"
            )

            print(f"\n{status_icon} {report['filepath']}")

            if report["issues"]:
                print("  Issues:")
                for issue in report["issues"]:
                    line_info = f" (line {issue.get('line', 'N/A')})" if "line" in issue else ""
                    print(f"    • {issue.get('message', 'Unknown issue')}{line_info}")

            if report["warnings"]:
                print("  Warnings:")
                for warning in report["warnings"]:
                    line_info = f" (line {warning.get('line', 'N/A')})" if "line" in warning else ""
                    print(f"    • {warning.get('message', 'Unknown warning')}{line_info}")

    print("\n" + "=" * 70)


def main(argv: List[str] = None) -> int:
    """Run code review on files passed as arguments or entire src directory.

    Args:
        argv: Command line arguments

    Returns:
        Exit code (0 for success, 1 for issues found)
    """
    if argv is None:
        argv = sys.argv[1:]

    agent = CodeReviewAgent()

    # If specific files provided, review them
    if argv:
        reports = []
        for filepath in argv:
            if filepath.endswith(".py"):
                logger.info(f"Reviewing {filepath}")
                report = agent.review_file(filepath)
                reports.append(report)
    else:
        # Review entire src directory
        logger.info("Reviewing src directory...")
        reports = agent.review_directory("src")

    if not reports:
        logger.warning("No Python files to review")
        return 0

    summary = agent.generate_summary(reports)
    print_report(summary)

    # Return non-zero exit code if issues found
    if summary["total_issues"] > 0:
        logger.error(f"Code review failed with {summary['total_issues']} issue(s)")
        return 1

    if summary["total_warnings"] > 0:
        logger.warning(f"Code review passed with {summary['total_warnings']} warning(s)")
        return 0

    logger.info("Code review passed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())

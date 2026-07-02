"""Code Review Agent for automated code quality analysis."""

import ast
import logging
from pathlib import Path
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CodeReviewAgent:
    """Automated code review agent for quality checks."""

    def __init__(self: "CodeReviewAgent") -> None:
        """Initialize the code review agent."""
        self.issues: List[Dict[str, Any]] = []
        self.warnings: List[Dict[str, Any]] = []
        logger.info("CodeReviewAgent initialized")

    def review_file(self: "CodeReviewAgent", filepath: str) -> Dict[str, Any]:
        """Perform comprehensive code review on a file.

        Args:
            filepath: Path to the Python file to review

        Returns:
            Dictionary containing review results
        """
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            report: Dict[str, Any] = {
                "filepath": filepath,
                "issues": [],
                "warnings": [],
                "status": "passed",
            }

            # Check for docstrings
            self._check_docstrings(filepath, content, report)

            # Check for type hints
            self._check_type_hints(filepath, content, report)

            # Check for magic numbers
            self._check_magic_numbers(filepath, content, report)

            # Check function complexity
            self._check_function_complexity(filepath, content, report)

            # Check for unused variables
            self._check_unused_variables(filepath, content, report)

            # Set status based on issues
            if report["issues"]:
                report["status"] = "failed"
            elif report["warnings"]:
                report["status"] = "warning"

            return report

        except Exception as e:
            logger.error(f"Error reviewing {filepath}: {e}")
            return {
                "filepath": filepath,
                "issues": [{"message": f"Review failed: {str(e)}"}],
                "status": "error",
            }

    def _check_docstrings(
        self: "CodeReviewAgent",
        filepath: str,
        content: str,
        report: Dict[str, Any],
    ) -> None:
        """Check for missing docstrings in functions and classes."""
        try:
            tree = ast.parse(content)

            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    # Skip private functions and test functions
                    if node.name.startswith("_") or node.name.startswith("test_"):
                        continue

                    if not ast.get_docstring(node):
                        report["warnings"].append(
                            {
                                "type": "missing_docstring",
                                "function": node.name,
                                "line": node.lineno,
                                "message": f"Function '{node.name}' missing docstring",
                            }
                        )

                elif isinstance(node, ast.ClassDef):
                    if not ast.get_docstring(node):
                        report["warnings"].append(
                            {
                                "type": "missing_docstring",
                                "class": node.name,
                                "line": node.lineno,
                                "message": f"Class '{node.name}' missing docstring",
                            }
                        )

        except SyntaxError as e:
            report["issues"].append({"type": "syntax_error", "message": f"Syntax error: {str(e)}"})

    def _check_type_hints(
        self: "CodeReviewAgent",
        filepath: str,
        content: str,
        report: Dict[str, Any],
    ) -> None:
        """Check for missing type hints in function signatures."""
        try:
            tree = ast.parse(content)

            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if node.name.startswith("_") or node.name.startswith("test_"):
                        continue

                    # Check for return type hint
                    if node.returns is None:
                        report["warnings"].append(
                            {
                                "type": "missing_return_type",
                                "function": node.name,
                                "line": node.lineno,
                                "message": f"Function '{node.name}' missing return type hint",
                            }
                        )

                    # Check for argument type hints
                    for arg in node.args.args:
                        if arg.arg == "self":
                            continue
                        if arg.annotation is None:
                            report["warnings"].append(
                                {
                                    "type": "missing_arg_type",
                                    "function": node.name,
                                    "argument": arg.arg,
                                    "line": node.lineno,
                                    "message": f"Argument '{arg.arg}' missing type hint",
                                }
                            )

        except SyntaxError:
            pass

    def _check_magic_numbers(
        self: "CodeReviewAgent",
        filepath: str,
        content: str,
        report: Dict[str, Any],
    ) -> None:
        """Check for magic numbers in code."""
        try:
            tree = ast.parse(content)

            for node in ast.walk(tree):
                if isinstance(node, ast.Constant):
                    if isinstance(node.value, (int, float)):
                        # Allow common magic numbers
                        if node.value not in (0, 1, -1, 2, 100):
                            report["warnings"].append(
                                {
                                    "type": "magic_number",
                                    "value": node.value,
                                    "line": node.lineno,
                                    "message": f"Magic number {node.value} detected, consider using named constant",
                                }
                            )

        except SyntaxError:
            pass

    def _check_function_complexity(
        self: "CodeReviewAgent",
        filepath: str,
        content: str,
        report: Dict[str, Any],
    ) -> None:
        """Check for overly complex functions."""
        try:
            tree = ast.parse(content)

            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    # Count decision points (if, for, while, except, etc.)
                    complexity = self._calculate_complexity(node)

                    if complexity > 10:
                        report["issues"].append(
                            {
                                "type": "high_complexity",
                                "function": node.name,
                                "complexity": complexity,
                                "line": node.lineno,
                                "message": f"Function '{node.name}' has high complexity ({complexity}), consider refactoring",
                            }
                        )
                    elif complexity > 7:
                        report["warnings"].append(
                            {
                                "type": "moderate_complexity",
                                "function": node.name,
                                "complexity": complexity,
                                "line": node.lineno,
                                "message": f"Function '{node.name}' has moderate complexity ({complexity})",
                            }
                        )

        except SyntaxError:
            pass

    @staticmethod
    def _calculate_complexity(node: ast.AST) -> int:
        """Calculate cyclomatic complexity of a function."""
        complexity = 1
        for child in ast.walk(node):
            if isinstance(
                child,
                (
                    ast.If,
                    ast.For,
                    ast.While,
                    ast.ExceptHandler,
                    ast.With,
                ),
            ):
                complexity += 1
        return complexity

    def _check_unused_variables(
        self: "CodeReviewAgent",
        filepath: str,
        content: str,
        report: Dict[str, Any],
    ) -> None:
        """Check for potentially unused variables."""
        try:
            tree = ast.parse(content)

            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    # Basic check for variables assigned but not used
                    assigned = set()
                    used = set()

                    for child in ast.walk(node):
                        if isinstance(child, ast.Assign):
                            for target in child.targets:
                                if isinstance(target, ast.Name):
                                    assigned.add(target.id)

                        elif isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load):
                            used.add(child.id)

                    unused = assigned - used
                    for var in unused:
                        if not var.startswith("_"):
                            report["warnings"].append(
                                {
                                    "type": "unused_variable",
                                    "function": node.name,
                                    "variable": var,
                                    "message": f"Variable '{var}' may be unused",
                                }
                            )

        except SyntaxError:
            pass

    def review_directory(self: "CodeReviewAgent", directory: str) -> List[Dict[str, Any]]:
        """Review all Python files in a directory.

        Args:
            directory: Path to directory to review

        Returns:
            List of review reports for each file
        """
        reports = []
        path = Path(directory)

        for py_file in path.rglob("*.py"):
            # Skip test files and __pycache__
            if "test_" in py_file.name or "__pycache__" in str(py_file):
                continue

            logger.info(f"Reviewing {py_file}")
            report = self.review_file(str(py_file))
            reports.append(report)

        return reports

    def generate_summary(self: "CodeReviewAgent", reports: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate summary of review reports.

        Args:
            reports: List of review reports

        Returns:
            Summary dictionary
        """
        summary: Dict[str, Any] = {
            "total_files": len(reports),
            "passed": 0,
            "warnings": 0,
            "failed": 0,
            "total_issues": 0,
            "total_warnings": 0,
            "files": reports,
        }

        for report in reports:
            if report["status"] == "passed":
                summary["passed"] += 1
            elif report["status"] == "warning":
                summary["warnings"] += 1
            elif report["status"] == "failed":
                summary["failed"] += 1

            summary["total_issues"] += len(report["issues"])
            summary["total_warnings"] += len(report["warnings"])

        return summary

"""Test suite for Code Review Agent."""

import pytest
from src.code_review_agent import CodeReviewAgent


class TestCodeReviewAgent:
    """Test CodeReviewAgent class."""

    @pytest.fixture
    def agent(self) -> CodeReviewAgent:
        """Create CodeReviewAgent instance for testing."""
        return CodeReviewAgent()

    def test_initialization(self, agent: CodeReviewAgent) -> None:
        """Test agent initialization."""
        assert agent.issues == []
        assert agent.warnings == []

    def test_check_docstrings(self, tmp_path, agent: CodeReviewAgent) -> None:
        """Test docstring checking."""
        test_file = tmp_path / "test_module.py"
        test_file.write_text('''
def function_without_docstring():
    """This has a docstring."""
    pass

def another_function():
    pass
''')

        report = agent.review_file(str(test_file))
        assert report["status"] in ["passed", "warning"]
        # Should have warning about missing docstring
        assert any(w["type"] == "missing_docstring" for w in report["warnings"])

    def test_check_type_hints(self, tmp_path, agent: CodeReviewAgent) -> None:
        """Test type hints checking."""
        test_file = tmp_path / "test_types.py"
        test_file.write_text('''
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b
''')

        report = agent.review_file(str(test_file))
        # Should have warnings about missing type hints in subtract
        assert any(w["type"] == "missing_arg_type" for w in report["warnings"])

    def test_check_function_complexity(self, tmp_path, agent: CodeReviewAgent) -> None:
        """Test function complexity checking."""
        test_file = tmp_path / "test_complexity.py"
        test_file.write_text('''
def complex_function(x: int) -> int:
    """A complex function."""
    if x > 0:
        if x > 10:
            if x > 20:
                if x > 30:
                    if x > 40:
                        if x > 50:
                            if x > 60:
                                if x > 70:
                                    if x > 80:
                                        if x > 90:
                                            return x
    return 0
''')

        report = agent.review_file(str(test_file))
        # Should have issue about high complexity
        assert any(i["type"] == "high_complexity" for i in report["issues"])

    def test_review_nonexistent_file(self, agent: CodeReviewAgent) -> None:
        """Test reviewing nonexistent file."""
        report = agent.review_file("/nonexistent/file.py")
        assert report["status"] == "error"
        assert len(report["issues"]) > 0

    def test_generate_summary(self, agent: CodeReviewAgent) -> None:
        """Test summary generation."""
        reports = [
            {
                "filepath": "file1.py",
                "issues": [],
                "warnings": [],
                "status": "passed",
            },
            {
                "filepath": "file2.py",
                "issues": [{"message": "Issue 1"}],
                "warnings": [],
                "status": "failed",
            },
        ]

        summary = agent.generate_summary(reports)
        assert summary["total_files"] == 2
        assert summary["passed"] == 1
        assert summary["failed"] == 1
        assert summary["total_issues"] == 1

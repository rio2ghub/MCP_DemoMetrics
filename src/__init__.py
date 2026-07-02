"""MCP Demo Metrics Package - Seaborn Visualization Module.

This package provides tools for metrics processing and heatmap visualization.

Modules:
    config: Configuration and logging setup
    metrics: Metrics processing and validation
    visualizer: Heatmap visualization utilities
    code_review_agent: Automated code quality analysis
"""

from .code_review_agent import CodeReviewAgent
from .config import __version__
from .metrics import MetricsProcessor
from .visualizer import HeatmapVisualizer

__all__ = [
    "__version__",
    "MetricsProcessor",
    "HeatmapVisualizer",
    "CodeReviewAgent",
]

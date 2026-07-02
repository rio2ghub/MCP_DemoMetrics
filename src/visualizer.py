"""Visualization module for creating seaborn heatmap visualizations."""

import logging
from typing import Any, Dict, Optional

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

logger = logging.getLogger(__name__)


class HeatmapVisualizer:
    """Create seaborn heatmap visualizations for metrics."""

    def __init__(
        self: "HeatmapVisualizer",
        figsize: tuple[int, int] = (12, 8),
        style: str = "darkgrid",
    ) -> None:
        """Initialize the heatmap visualizer.

        Args:
            figsize: Figure size as (width, height)
            style: Seaborn style to use
        """
        self.figsize = figsize
        self.style = style
        sns.set_style(self.style)
        logger.info(f"HeatmapVisualizer initialized with style: {self.style}")

    def create_heatmap(
        self: "HeatmapVisualizer",
        data: pd.DataFrame,
        title: str = "Metrics Heatmap",
        cmap: str = "coolwarm",
        annot: bool = True,
        fmt: str = ".2f",
        cbar_kws: Optional[Dict[str, Any]] = None,
    ) -> plt.Figure:
        """Create a heatmap visualization.

        Args:
            data: DataFrame containing data to visualize
            title: Title for the heatmap
            cmap: Colormap to use
            annot: Whether to annotate cells
            fmt: Format string for annotations
            cbar_kws: Keyword arguments for colorbar

        Returns:
            matplotlib Figure object

        Raises:
            ValueError: If data is empty
        """
        if data.empty:
            raise ValueError("Cannot create heatmap with empty data")

        fig, ax = plt.subplots(figsize=self.figsize)

        if cbar_kws is None:
            cbar_kws = {"label": "Value"}

        sns.heatmap(
            data,
            cmap=cmap,
            annot=annot,
            fmt=fmt,
            cbar_kws=cbar_kws,
            ax=ax,
        )

        ax.set_title(title, fontsize=16, fontweight="bold")
        plt.tight_layout()

        logger.info(f"Heatmap created: {title}")
        return fig

    def save_figure(
        self: "HeatmapVisualizer",
        fig: plt.Figure,
        filepath: str,
        dpi: int = 300,
    ) -> None:
        """Save figure to file.

        Args:
            fig: Figure object to save
            filepath: Path where to save the figure
            dpi: Resolution in dots per inch

        Raises:
            IOError: If file cannot be written
        """
        try:
            fig.savefig(filepath, dpi=dpi, bbox_inches="tight")
            logger.info(f"Figure saved to {filepath}")
        except IOError as e:
            logger.error(f"Failed to save figure: {e}")
            raise

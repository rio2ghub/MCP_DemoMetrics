"""Example script demonstrating MCP Demo Metrics functionality."""

import logging

import numpy as np
import pandas as pd

from src import HeatmapVisualizer, MetricsProcessor

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Run demonstration of metrics visualization."""
    logger.info("Starting MCP Demo Metrics Example")

    # Create sample metrics data
    np.random.seed(42)
    metrics_data = pd.DataFrame(
        np.random.randn(8, 6) * 10 + 50,
        columns=["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"],
        index=[
            "Accuracy",
            "Precision",
            "Recall",
            "F1-Score",
            "AUC",
            "Latency",
            "Throughput",
            "ErrorRate",
        ],
    )

    logger.info(f"Generated metrics data with shape {metrics_data.shape}")
    logger.info(f"\nMetrics Data:\n{metrics_data}")

    # Process data
    processor = MetricsProcessor()
    processor.load_data(metrics_data)

    if processor.validate_data():
        logger.info("Data validation passed")
    else:
        logger.error("Data validation failed")
        return

    # Create visualization
    visualizer = HeatmapVisualizer(figsize=(12, 8))

    try:
        fig = visualizer.create_heatmap(
            metrics_data,
            title="Performance Metrics Heatmap",
            cmap="RdYlGn",
            annot=True,
            fmt=".1f",
        )

        # Save the figure
        output_path = "demo_heatmap.png"
        visualizer.save_figure(fig, output_path, dpi=300)
        logger.info(f"Heatmap saved to {output_path}")

    except ValueError as e:
        logger.error(f"Error creating heatmap: {e}")


if __name__ == "__main__":
    main()

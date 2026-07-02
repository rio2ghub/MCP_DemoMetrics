"""Metrics processing module for data validation and preparation."""

import logging
from typing import Optional

import pandas as pd

logger = logging.getLogger(__name__)


class MetricsProcessor:
    """Process and prepare metrics data for visualization."""

    def __init__(self: "MetricsProcessor") -> None:
        """Initialize the metrics processor."""
        self.data: Optional[pd.DataFrame] = None
        logger.info("MetricsProcessor initialized")

    def load_data(self: "MetricsProcessor", data: pd.DataFrame) -> None:
        """Load data into the processor.

        Args:
            data: DataFrame containing metrics data

        Raises:
            ValueError: If data is empty or invalid
        """
        if data.empty:
            raise ValueError("Input data cannot be empty")
        self.data = data
        logger.info(f"Loaded data with shape {data.shape}")

    def validate_data(self: "MetricsProcessor") -> bool:
        """Validate the loaded data.

        Returns:
            True if data is valid, False otherwise
        """
        if self.data is None:
            logger.warning("No data loaded")
            return False

        if self.data.empty:
            logger.warning("Data is empty")
            return False

        return True

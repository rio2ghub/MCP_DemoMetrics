"""Test suite for MCP Demo Metrics package."""

import pytest
import numpy as np
import pandas as pd
from src import HeatmapVisualizer, MetricsProcessor


class TestMetricsProcessor:
    """Test MetricsProcessor class."""

    def test_initialization(self) -> None:
        """Test MetricsProcessor initialization."""
        processor = MetricsProcessor()
        assert processor.data is None

    def test_load_data(self) -> None:
        """Test loading data into processor."""
        processor = MetricsProcessor()
        data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        processor.load_data(data)
        assert processor.data is not None
        assert processor.data.shape == (3, 2)

    def test_load_empty_data_raises_error(self) -> None:
        """Test that loading empty data raises ValueError."""
        processor = MetricsProcessor()
        with pytest.raises(ValueError):
            processor.load_data(pd.DataFrame())

    def test_validate_data_no_data(self) -> None:
        """Test data validation with no data loaded."""
        processor = MetricsProcessor()
        assert processor.validate_data() is False

    def test_validate_data_with_valid_data(self) -> None:
        """Test data validation with valid data."""
        processor = MetricsProcessor()
        data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        processor.load_data(data)
        assert processor.validate_data() is True


class TestHeatmapVisualizer:
    """Test HeatmapVisualizer class."""

    @pytest.fixture
    def visualizer(self) -> HeatmapVisualizer:
        """Create a HeatmapVisualizer instance for testing."""
        return HeatmapVisualizer(figsize=(10, 8))

    @pytest.fixture
    def sample_data(self) -> pd.DataFrame:
        """Create sample data for testing."""
        return pd.DataFrame(
            np.random.randn(5, 5),
            columns=["A", "B", "C", "D", "E"],
            index=["Row1", "Row2", "Row3", "Row4", "Row5"],
        )

    def test_initialization(self, visualizer: HeatmapVisualizer) -> None:
        """Test HeatmapVisualizer initialization."""
        assert visualizer.figsize == (10, 8)
        assert visualizer.style == "darkgrid"

    def test_create_heatmap(self, visualizer: HeatmapVisualizer, sample_data: pd.DataFrame) -> None:
        """Test heatmap creation."""
        fig = visualizer.create_heatmap(sample_data, title="Test Heatmap")
        assert fig is not None

    def test_create_heatmap_empty_data(self, visualizer: HeatmapVisualizer) -> None:
        """Test that creating heatmap with empty data raises ValueError."""
        with pytest.raises(ValueError):
            visualizer.create_heatmap(pd.DataFrame())

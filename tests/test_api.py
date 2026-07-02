"""Test suite for FastAPI endpoints."""

import pytest
import numpy as np
from fastapi.testclient import TestClient

from src.api import app


@pytest.fixture
def client() -> TestClient:
    """Create a FastAPI test client."""
    return TestClient(app)


@pytest.fixture
def sample_metrics_data() -> dict:
    """Create sample metrics data for testing."""
    return {
        "values": np.random.randn(5, 5).tolist(),
    }


class TestHealthEndpoint:
    """Test health check endpoint."""

    def test_health_check(self, client: TestClient) -> None:
        """Test health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "MCP Demo Metrics API"


class TestMetricsEndpoints:
    """Test metrics endpoints."""

    def test_validate_metrics_success(self, client: TestClient, sample_metrics_data: dict) -> None:
        """Test successful metrics validation."""
        response = client.post("/api/v1/metrics/validate", json=sample_metrics_data)
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "valid"
        assert "shape" in data

    def test_validate_metrics_empty_data(self, client: TestClient) -> None:
        """Test validation with empty data."""
        response = client.post(
            "/api/v1/metrics/validate",
            json={"values": []},
        )
        assert response.status_code == 400

    def test_validate_metrics_missing_values(self, client: TestClient) -> None:
        """Test validation with missing values key."""
        response = client.post("/api/v1/metrics/validate", json={})
        assert response.status_code == 400

    def test_metrics_info(self, client: TestClient) -> None:
        """Test metrics info endpoint."""
        response = client.get("/api/v1/metrics/info")
        assert response.status_code == 200
        data = response.json()
        assert "capabilities" in data
        assert "supported_formats" in data


class TestVisualizationEndpoints:
    """Test visualization endpoints."""

    def test_visualization_info(self, client: TestClient) -> None:
        """Test visualization info endpoint."""
        response = client.get("/api/v1/visualization/info")
        assert response.status_code == 200
        data = response.json()
        assert data["visualizer"] == "HeatmapVisualizer"
        assert "supported_colormaps" in data
        assert "export_formats" in data

    def test_generate_heatmap_success(self, client: TestClient, sample_metrics_data: dict) -> None:
        """Test successful heatmap generation."""
        request_data = {
            **sample_metrics_data,
            "title": "Test Heatmap",
            "cmap": "coolwarm",
        }
        response = client.post("/api/v1/heatmap/generate", json=request_data)
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["title"] == "Test Heatmap"

    def test_generate_heatmap_custom_colormap(
        self, client: TestClient, sample_metrics_data: dict
    ) -> None:
        """Test heatmap generation with custom colormap."""
        request_data = {
            **sample_metrics_data,
            "title": "Viridis Heatmap",
            "cmap": "viridis",
        }
        response = client.post("/api/v1/heatmap/generate", json=request_data)
        assert response.status_code == 200
        data = response.json()
        assert data["cmap"] == "viridis"

    def test_generate_heatmap_empty_data(self, client: TestClient) -> None:
        """Test heatmap generation with empty data."""
        response = client.post(
            "/api/v1/heatmap/generate",
            json={"values": []},
        )
        assert response.status_code == 400

    def test_generate_heatmap_missing_values(self, client: TestClient) -> None:
        """Test heatmap generation with missing values."""
        response = client.post(
            "/api/v1/heatmap/generate",
            json={"title": "Invalid Heatmap"},
        )
        assert response.status_code == 400

    def test_download_heatmap_empty_data(self, client: TestClient) -> None:
        """Test heatmap download with empty data."""
        response = client.post(
            "/api/v1/heatmap/download",
            json={"values": []},
        )
        assert response.status_code == 400


class TestErrorHandling:
    """Test error handling in endpoints."""

    def test_404_not_found(self, client: TestClient) -> None:
        """Test 404 not found response."""
        response = client.get("/api/v1/nonexistent")
        assert response.status_code == 404

    def test_method_not_allowed(self, client: TestClient) -> None:
        """Test method not allowed response."""
        response = client.get("/api/v1/metrics/validate")
        assert response.status_code == 405

"""FastAPI application for MCP Demo Metrics."""

import io
import logging
from typing import Any, Dict

import pandas as pd
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse, JSONResponse

from . import HeatmapVisualizer, MetricsProcessor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI application
app: FastAPI = FastAPI(
    title="MCP Demo Metrics API",
    description="REST API for metrics processing and visualization",
    version="0.1.0",
)


# Pydantic models for request/response
class MetricsData(dict):
    """Metrics data model."""

    pass


class HeatmapRequest(dict):
    """Request model for heatmap generation."""

    pass


class HeatmapResponse(dict):
    """Response model for heatmap generation."""

    pass


class HealthResponse(dict):
    """Health check response model."""

    pass


# Health check endpoint
@app.get("/health", response_model=Dict[str, Any])
async def health_check() -> Dict[str, str]:
    """Health check endpoint.

    Returns:
        Health status
    """
    return {
        "status": "healthy",
        "service": "MCP Demo Metrics API",
        "version": "0.1.0",
    }


# Metrics processing endpoints
@app.post("/api/v1/metrics/validate")
async def validate_metrics(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate metrics data.

    Args:
        data: Metrics data as dictionary

    Returns:
        Validation result

    Raises:
        HTTPException: If validation fails
    """
    try:
        # Convert to DataFrame
        if "values" not in data:
            raise ValueError("Missing 'values' key in data")

        df = pd.DataFrame(data["values"])

        if df.empty:
            raise ValueError("Data cannot be empty")

        processor = MetricsProcessor()
        processor.load_data(df)

        if not processor.validate_data():
            raise ValueError("Data validation failed")

        logger.info(f"Validated metrics data with shape {df.shape}")

        return {
            "status": "valid",
            "message": "Metrics data is valid",
            "shape": {"rows": df.shape[0], "columns": df.shape[1]},
            "columns": list(df.columns),
        }

    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Validation error: {str(e)}",
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


@app.post("/api/v1/heatmap/generate")
async def generate_heatmap(request: Dict[str, Any]) -> Dict[str, Any]:
    """Generate heatmap visualization.

    Args:
        request: Request containing:
            - values: 2D array of data
            - title: Heatmap title
            - cmap: Colormap name (default: coolwarm)
            - annot: Whether to annotate cells (default: true)
            - fmt: Format string for annotations (default: .2f)

    Returns:
        Heatmap metadata

    Raises:
        HTTPException: If generation fails
    """
    try:
        # Extract parameters
        if "values" not in request:
            raise ValueError("Missing 'values' key in request")

        data = request.get("values")
        title = request.get("title", "Metrics Heatmap")
        cmap = request.get("cmap", "coolwarm")
        annot = request.get("annot", True)
        fmt = request.get("fmt", ".2f")

        # Convert to DataFrame
        df = pd.DataFrame(data)

        if df.empty:
            raise ValueError("Data cannot be empty")

        # Create visualizer
        visualizer = HeatmapVisualizer(figsize=(12, 8))

        # Generate heatmap
        fig = visualizer.create_heatmap(
            df,
            title=title,
            cmap=cmap,
            annot=annot,
            fmt=fmt,
        )

        # Save to bytes buffer
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png", dpi=100, bbox_inches="tight")
        buffer.seek(0)

        logger.info(f"Generated heatmap: {title}")

        return {
            "status": "success",
            "message": "Heatmap generated successfully",
            "title": title,
            "shape": {"rows": df.shape[0], "columns": df.shape[1]},
            "cmap": cmap,
        }

    except ValueError as e:
        logger.error(f"Generation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Generation error: {str(e)}",
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


@app.post("/api/v1/heatmap/download")
async def download_heatmap(request: Dict[str, Any]) -> FileResponse:
    """Download heatmap as PNG file.

    Args:
        request: Request containing data and parameters

    Returns:
        PNG file response

    Raises:
        HTTPException: If download fails
    """
    try:
        # Extract parameters
        if "values" not in request:
            raise ValueError("Missing 'values' key in request")

        data = request.get("values")
        title = request.get("title", "heatmap")
        cmap = request.get("cmap", "coolwarm")
        annot = request.get("annot", True)
        fmt = request.get("fmt", ".2f")

        # Convert to DataFrame
        df = pd.DataFrame(data)

        if df.empty:
            raise ValueError("Data cannot be empty")

        # Create visualizer
        visualizer = HeatmapVisualizer(figsize=(12, 8))

        # Generate heatmap
        fig = visualizer.create_heatmap(
            df,
            title=title,
            cmap=cmap,
            annot=annot,
            fmt=fmt,
        )

        # Save to bytes buffer
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png", dpi=300, bbox_inches="tight")
        buffer.seek(0)

        # Create filename
        filename = f"{title.lower().replace(' ', '_')}.png"

        logger.info(f"Downloaded heatmap: {filename}")

        return FileResponse(
            path=buffer,
            media_type="image/png",
            filename=filename,
        )

    except ValueError as e:
        logger.error(f"Download error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Download error: {str(e)}",
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


@app.get("/api/v1/metrics/info")
async def metrics_info() -> Dict[str, Any]:
    """Get information about the metrics processing engine.

    Returns:
        Information about supported operations
    """
    return {
        "processor": "MetricsProcessor",
        "capabilities": [
            "data_loading",
            "validation",
            "transformation",
        ],
        "supported_formats": [
            "csv",
            "json",
            "pandas_dataframe",
        ],
        "constraints": {
            "min_rows": 1,
            "max_rows": 1000000,
            "min_columns": 1,
            "max_columns": 1000,
        },
    }


@app.get("/api/v1/visualization/info")
async def visualization_info() -> Dict[str, Any]:
    """Get information about visualization capabilities.

    Returns:
        Information about supported visualizations
    """
    return {
        "visualizer": "HeatmapVisualizer",
        "types": ["heatmap"],
        "supported_colormaps": [
            "coolwarm",
            "viridis",
            "plasma",
            "inferno",
            "RdYlGn",
            "PiYG",
            "BrBG",
        ],
        "export_formats": [
            "png",
            "pdf",
            "svg",
        ],
        "default_resolution": "100 dpi",
        "high_resolution": "300 dpi",
    }


# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Any, exc: HTTPException) -> JSONResponse:
    """Handle HTTP exceptions.

    Args:
        request: Request object
        exc: HTTPException

    Returns:
        JSON response with error details
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Any, exc: Exception) -> JSONResponse:
    """Handle general exceptions.

    Args:
        request: Request object
        exc: Exception

    Returns:
        JSON response with error details
    """
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "status_code": 500,
        },
    )

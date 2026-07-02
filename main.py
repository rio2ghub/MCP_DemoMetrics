"""FastAPI server runner for MCP Demo Metrics."""

import logging

import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    """Run FastAPI development server."""
    logger.info("Starting MCP Demo Metrics API server...")

    uvicorn.run(
        "src.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )


if __name__ == "__main__":
    main()

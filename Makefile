.PHONY: help install install-dev format lint type-check security-check test clean pre-commit-install demo docker-build docker-run code-review api

help:
	@echo "MCP Demo Metrics - Available Commands"
	@echo "====================================="
	@echo "  make install           - Install runtime dependencies"
	@echo "  make install-dev       - Install all dependencies including dev tools"
	@echo "  make pre-commit-install - Setup pre-commit hooks"
	@echo "  make format            - Format code with black and isort"
	@echo "  make lint              - Run flake8 and pylint checks"
	@echo "  make type-check        - Run mypy type checking"
	@echo "  make security-check    - Run bandit and safety checks"
	@echo "  make code-review       - Run CodeReview Agent analysis"
	@echo "  make test              - Run pytest with coverage"
	@echo "  make demo              - Run demo example"
	@echo "  make api               - Start FastAPI server (http://localhost:8000)"
	@echo "  make docker-build      - Build Docker image"
	@echo "  make docker-run        - Run Docker container"
	@echo "  make clean             - Clean up generated files"
	@echo "  make all               - Run all checks (format, lint, type-check, test, code-review)"

install:
	pip install --upgrade pip
	pip install -r requirements.txt

install-dev:
	pip install --upgrade pip
	pip install -r requirements-dev.txt

pre-commit-install:
	pre-commit install
	@echo "Pre-commit hooks installed successfully"

format:
	black src/ tests/
	isort src/ tests/
	@echo "Code formatting complete"

lint:
	flake8 src/
	pylint src/ --exit-zero
	@echo "Linting checks complete"

type-check:
	mypy src/
	@echo "Type checking complete"

security-check:
	bandit -r src/ -c .bandit
	safety check --file requirements.txt
	@echo "Security checks complete"

code-review:
	python code_review.py
	@echo "Code review analysis complete"

test:
	pytest tests/ --cov=src --cov-report=html --cov-report=term-missing
	@echo "Tests complete - Coverage report in htmlcov/index.html"

demo:
	python demo_example.py

api:
	python main.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	@echo "Cleanup complete"

docker-build:
	docker build -t mcp-demo-metrics:latest .

docker-run:
	docker run --rm -v $(PWD)/outputs:/app/outputs mcp-demo-metrics:latest

all: format lint type-check security-check code-review test
	@echo "All checks passed successfully!"

.DEFAULT_GOAL := help

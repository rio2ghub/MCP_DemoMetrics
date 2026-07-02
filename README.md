# MCP Demo Metrics - Python Project with Guardrails

Senior Executive Demo showcasing MCP Server Client in Python with comprehensive quality guardrails, seaborn visualizations, Docker containerization, and GitHub Actions CI/CD.

---

## 📋 Application Scope

**MCP Demo Metrics** is a production-ready Python framework designed to demonstrate best practices in enterprise software development. It provides a complete end-to-end solution for metrics visualization, code quality management, and automated deployment with industry-standard guardrails.

### What This Project Does

This application serves as a comprehensive reference implementation for:
- **Metrics Processing & Visualization**: Load, process, and visualize business metrics using professional heatmaps
- **Code Quality Enforcement**: Automatically enforce coding standards before code reaches production
- **Continuous Integration/Deployment**: Automate testing, security scanning, and code review in a containerized environment
- **Enterprise Readiness**: Demonstrate production-grade practices including type safety, security scanning, and comprehensive testing

### Target Use Cases

- **Executive Demonstrations**: Showcase modern Python development practices to stakeholders
- **Metrics Dashboard Backend**: Serve as foundation for data visualization platforms
- **Educational Reference**: Learn enterprise Python development patterns
- **CI/CD Pipeline Template**: Use as a starting point for new Python projects with guardrails

---

## ✨ Feature Description

### Core Capabilities

#### 1. **Metrics Processing Engine**
- Load and validate business metrics from various data sources
- Support for time-series and cross-sectional data
- Data validation with error handling and logging
- Extensible processor architecture for custom transformations

#### 2. **Professional Visualization Suite**
- **Heatmap Visualizations**: Create publication-ready heatmaps using Seaborn
- **Customizable Styling**: Configure colors, annotations, and labels
- **Export Capabilities**: Save visualizations in high-resolution formats (PNG, PDF, SVG)
- **Multi-metric Support**: Visualize multiple metrics simultaneously

#### 3. **Automated Code Quality Checks**
- **Static Analysis**: Detect code issues before runtime
- **Type Safety**: Full type checking with MyPy in strict mode
- **Security Scanning**: Identify vulnerabilities in dependencies and code
- **Coverage Enforcement**: Require minimum 80% test coverage
- **Custom Code Review**: Agent-based analysis of code patterns
#### 6. **RESTful API with FastAPI**
- **HTTP Endpoints**: Expose metrics processing and visualization as REST APIs
- **OpenAPI Documentation**: Auto-generated interactive API documentation (Swagger UI, ReDoc)
- **Data Validation**: Pydantic models ensure request/response type safety
- **Error Handling**: Comprehensive error responses with meaningful messages
- **Production Ready**: Uvicorn ASGI server for high performance deployment
#### 4. **Pre-commit & Pre-push Guardrails**
- **Automatic Formatting**: Black and isort apply code style consistently
- **Linting Checks**: Flake8 and Pylint catch common issues
- **Code Review Hook**: CodeReview Agent performs pattern analysis
- **Instant Feedback**: Developers know issues before push attempts

#### 5. **GitHub Actions CI/CD Pipeline**
- **Multi-version Testing**: Test on Python 3.9, 3.10, and 3.11
- **Automated Security**: Bandit security scanning and dependency checks
- **Coverage Reporting**: Track test coverage trends over time
- **Merge Requirements**: Enforce code quality standards before merge

#### 6. **Docker & Container Support**
- **Containerized Execution**: Run in isolated, reproducible environments
- **Docker Compose**: Multi-service orchestration support
- **CI/CD Integration**: Containers built and tested automatically
- **Production Ready**: Optimized for deployment to cloud platforms

### Quality Assurance Features

| Feature | Tool | Purpose |
|---------|------|---------|
| Code Formatting | Black | Consistent, automated code style |
| Import Sorting | isort | Organized and standardized imports |
| Style Enforcement | Flake8 | PEP 8 compliance checking |
| Code Analysis | Pylint | Advanced pattern detection |
| Type Checking | MyPy | Static type safety verification |
| Security Scanning | Bandit | Detect security issues |
| Dependency Security | Safety | Identify vulnerable dependencies |
| Unit Testing | Pytest | Comprehensive test coverage |
| Code Review | CodeReview Agent | Custom quality gates |
| Pre-commit Hooks | pre-commit | Automated checks before commits |
| REST API | FastAPI | HTTP endpoints for metrics & visualization |
| API Server | Uvicorn | Production-grade ASGI server |
| API Documentation | Swagger UI, ReDoc | Interactive API documentation |

---

## Features

- 🛡️ **Code Guardrails**: Comprehensive linting, formatting, and type checking
- 🤖 **CodeReview Agent**: Automated code quality analysis (docstrings, type hints, complexity, magic numbers)
- 📊 **Seaborn Visualizations**: Professional heatmap and metric visualizations
- 🐳 **Docker Support**: Containerized deployment
- 🔄 **GitHub Actions CI/CD**: Automated testing and quality checks with code review
- 📈 **Test Coverage**: Pytest with >80% coverage requirement
- 🔒 **Security Scanning**: Bandit and Safety vulnerability checks

---

## 🏗️ System Architecture

### Core Components

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP Demo Metrics Platform                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────┐         ┌────────────────────────┐   │
│  │  Metrics Processor   │         │  Heatmap Visualizer    │   │
│  │  ├─ Data Loading     │         │  ├─ Heatmap Creation   │   │
│  │  ├─ Validation       │         │  ├─ Customization      │   │
│  │  └─ Transformation   │         │  └─ Export             │   │
│  └──────────────────────┘         └────────────────────────┘   │
│           │                                 │                   │
│           └─────────────────┬───────────────┘                   │
│                             │                                   │
│              ┌──────────────▼──────────────┐                    │
│              │   CodeReview Agent          │                    │
│              │  ├─ Docstring Analysis      │                    │
│              │  ├─ Type Hint Verification  │                    │
│              │  ├─ Complexity Detection    │                    │
│              │  └─ Pattern Matching        │                    │
│              └──────────────┬──────────────┘                    │
│                             │                                   │
│  ┌──────────────────────────▼────────────────────────────────┐ │
│  │           Quality Assurance Pipeline                      │ │
│  │  ┌──────────────┐ ┌──────────────┐ ┌────────────────────┐ │ │
│  │  │   Pre-commit │ │  GitHub      │ │  Docker            │ │ │
│  │  │   Hooks      │ │  Actions     │ │  Execution         │ │ │
│  │  └──────────────┘ └──────────────┘ └────────────────────┘ │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Data Input** → Metrics in CSV, JSON, or DataFrame format
2. **Processing** → MetricsProcessor validates and transforms data
3. **Visualization** → HeatmapVisualizer creates publication-ready outputs
4. **Quality Review** → CodeReview Agent analyzes code quality
5. **Testing** → Pytest ensures functionality and coverage
6. **Deployment** → Docker containers enable consistent execution

### Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Data Processing** | Pandas, NumPy | Handle and transform metrics data |
| **Visualization** | Seaborn, Matplotlib | Create professional visualizations |
| **Type Safety** | MyPy | Static type checking |
| **Code Quality** | Black, Flake8, Pylint | Code style and analysis |
| **Testing** | Pytest | Unit and integration testing |
| **Security** | Bandit, Safety | Vulnerability scanning |
| **Containerization** | Docker, Docker Compose | Environment isolation |
| **CI/CD** | GitHub Actions | Automated deployment |
| **Code Review** | CodeReview Agent | Automated pattern analysis |

---

## 🎯 Key Technical Specifications

### Language & Framework
- **Primary Language**: Python 3.9+
- **Package Manager**: pip with pyproject.toml
- **Build System**: setuptools

### Quality Metrics
- **Minimum Test Coverage**: 80%
- **Type Checking**: Strict mode (MyPy)
- **Code Complexity**: Cyclomatic complexity ≤ 10
- **Line Length**: Maximum 100 characters

### Performance Characteristics
- **Heatmap Generation**: <500ms for typical datasets
- **Code Review Analysis**: <2s for average file
- **Test Suite Execution**: <30s for full suite
- **Pre-commit Hooks**: <10s average run time

### Security Standards
- **Dependency Scanning**: Automated security audits
- **Code Analysis**: Bandit security patterns
- **Access Control**: Environment-based configurations
- **Logging**: Comprehensive audit trails

---

## Project Structure

```
MCP_DemoMetrics/
├── src/                          # Main source code
│   └── __init__.py              # Core modules (HeatmapVisualizer, MetricsProcessor)
├── tests/                        # Test suite
│   └── test_visualizer.py       # Unit tests
├── .github/
│   └── workflows/
│       └── python-guardrails.yml # CI/CD pipeline
├── pyproject.toml               # Project configuration & dependencies
├── requirements.txt             # Runtime dependencies
├── requirements-dev.txt         # Development dependencies
├── .pre-commit-config.yaml      # Pre-commit hooks
├── .bandit                       # Bandit security configuration
├── .flake8                       # Flake8 linter configuration
├── .gitignore                   # Git ignore rules
└── demo_example.py              # Example script

```

## Guardrails Configuration

### Linting & Formatting
- **Black**: Code formatter (line length: 100)
- **Flake8**: Style guide enforcement
- **Pylint**: Code analysis
- **isort**: Import statement sorting

### Type Checking
- **MyPy**: Static type checking with strict mode

### Code Review
- **CodeReview Agent**: Automated analysis for:
  - Missing docstrings in functions and classes
  - Missing type hints in function signatures
  - Magic numbers that should be constants
  - Function complexity detection (cyclomatic complexity)
  - Unused variable detection
  - Comprehensive issue and warning reporting

### Testing
- **Pytest**: Unit testing with >80% coverage requirement
- **Pytest-Cov**: Coverage reporting

### Security
- **Bandit**: Security issue detection
- **Safety**: Dependency vulnerability scanning
- **Pre-commit hooks**: Automated checks before commits

## Quick Start

### 1. Setup Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip
```

### 2. Install Dependencies

```bash
# Install runtime dependencies
pip install -r requirements.txt

# Install development dependencies (includes all guardrails)
pip install -r requirements-dev.txt
```

### 3. Setup Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run all hooks on all files (optional)
pre-commit run --all-files
```

### 4. Run Tests

```bash
# Run all tests with coverage
pytest tests/ --cov=src --cov-report=html

# View coverage report
# Open htmlcov/index.html in browser
```

### 5. Run Guardrails Checks

```bash
# Format code with Black
black src/ tests/

# Check imports with isort
isort src/ tests/

# Run all linters
flake8 src/
pylint src/

# Type checking
mypy src/

# Security scanning
bandit -r src/
safety check --file requirements.txt

# Run CodeReview Agent
python code_review.py
```

### 6. Run Example

```bash
python demo_example.py
```

### 7. Start API Server

```bash
# Development mode with auto-reload
python main.py

# Or access API documentation
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

---

## 🌐 REST API with FastAPI

### Quick Start

The application provides a RESTful API powered by FastAPI for programmatic access to metrics processing and visualization capabilities.

```bash
# Start the API server
python main.py

# Server runs on http://localhost:8000
# Interactive docs: http://localhost:8000/docs
```

### Core API Endpoints

#### Health Check
```bash
GET /health
```
Returns service status and version.

#### Validate Metrics Data
```bash
POST /api/v1/metrics/validate
```
Validates metrics data structure and returns information.

Request:
```json
{
  "values": [[1, 2, 3], [4, 5, 6]]
}
```

#### Generate Heatmap
```bash
POST /api/v1/heatmap/generate
```
Generates heatmap visualization from metrics data.

Request:
```json
{
  "values": [[1, 2, 3], [4, 5, 6]],
  "title": "My Heatmap",
  "cmap": "coolwarm",
  "annot": true,
  "fmt": ".2f"
}
```

#### Download Heatmap
```bash
POST /api/v1/heatmap/download
```
Downloads heatmap as high-resolution PNG file (300 DPI).

#### Get Information
```bash
GET /api/v1/metrics/info
GET /api/v1/visualization/info
```
Returns capabilities and constraints of the API.

### API Examples

**Python Client:**
```python
import requests

# Validate data
response = requests.post(
    "http://localhost:8000/api/v1/metrics/validate",
    json={"values": [[1, 2], [3, 4]]}
)
print(response.json())

# Download heatmap
response = requests.post(
    "http://localhost:8000/api/v1/heatmap/download",
    json={"values": [[1, 2], [3, 4]], "title": "output"}
)
with open("heatmap.png", "wb") as f:
    f.write(response.content)
```

**cURL:**
```bash
# Check health
curl http://localhost:8000/health

# Validate metrics
curl -X POST http://localhost:8000/api/v1/metrics/validate \
  -H "Content-Type: application/json" \
  -d '{"values": [[1,2],[3,4]]}'
```

### Supported Colormaps

`coolwarm`, `viridis`, `plasma`, `inferno`, `RdYlGn`, `PiYG`, `BrBG`

### Export Formats

PNG (100 DPI, 300 DPI for downloads), PDF, SVG

---

## Dependencies

### Runtime
- **requests**: HTTP library
- **seaborn**: Statistical data visualization
- **matplotlib**: Plotting library
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **fastapi**: Web framework for building APIs
- **uvicorn**: ASGI server for running FastAPI

### Development
- **pytest**: Testing framework
- **pytest-cov**: Coverage plugin
- **httpx**: Async HTTP client for API testing
- **black**: Code formatter
- **flake8**: Style guide
- **pylint**: Code analyzer
- **mypy**: Type checker
- **pre-commit**: Git hook framework
- **bandit**: Security scanner
- **safety**: Dependency checker
- **isort**: Import sorter
- **autopep8**: Code formatter

---

## ⚡ Quick Reference Commands

| Goal | Command |
|------|---------|
| Setup dev environment | `make install-dev && make pre-commit-install` |
| Run all checks before push | `make all` |
| Format code automatically | `make format` |
| Run tests only | `make test` |
| Code review analysis | `make code-review` |
| Security checks | `make security-check` |
| Run demo script | `make demo` |
| Start FastAPI server | `make api` |
| Clean workspace | `make clean` |
| View all commands | `make help` |

---

## ❓ Frequently Asked Questions (FAQ)

### Installation & Setup

**Q: I get "command not found: python". What should I do?**
A: Ensure Python 3.9+ is installed. On Windows, use `python` or `py`. On macOS/Linux, you might need `python3`. Create an alias or add to PATH if needed.

**Q: Can I use Python 3.8?**
A: No, this project requires Python 3.9 or higher due to type annotation features and other modern Python constructs.

**Q: Do I need to install Docker to run the project?**
A: No, Docker is optional. You can run everything locally with Python and pip. Docker is useful for consistent deployment environments.

### Development

**Q: How do I add a new dependency?**
A: Add to `requirements.txt` (runtime) or `requirements-dev.txt` (development), then run `pip install -r requirements.txt` or `pip install -r requirements-dev.txt`.

**Q: Why does pre-commit run automatically?**
A: Pre-commit hooks are set up to ensure code quality standards before commits. Run `pre-commit install` to enable them.

**Q: Can I bypass pre-commit hooks?**
A: Yes, use `git commit --no-verify` to skip hooks, but this is not recommended for production code.

**Q: What if CodeReview Agent flags too many issues?**
A: The agent's warnings don't block commits, only critical issues do. Fix issues gradually while maintaining velocity.

### Code Quality

**Q: What's the minimum test coverage required?**
A: 80% minimum coverage is enforced. Use `pytest --cov=src --cov-report=html` to see coverage details.

**Q: Why do I need type hints everywhere?**
A: Type hints improve code clarity, enable better IDE support, and catch errors early. MyPy enforces strict typing.

**Q: How do I check my code quality locally?**
A: Run `make all` to execute format, lint, type-check, code review, and test in sequence.

### Visualization

**Q: How do I create custom heatmaps?**
A: Use the `HeatmapVisualizer` class with custom parameters. See `demo_example.py` for examples.

**Q: Can I export visualizations to PDF?**
A: Yes, change the file extension in `save_figure()` method: `.png`, `.pdf`, `.svg`, etc.

**Q: How do I handle large datasets?**
A: For datasets >1000x1000, consider aggregating data first. Current implementation is optimized for typical business metrics.

### Deployment

**Q: How do I deploy this to production?**
A: Build Docker image with `make docker-build`, then run with `make docker-run` or push to container registry.

**Q: Does the project support Kubernetes?**
A: Currently not, but Docker Compose is supported. Kubernetes templates are on the roadmap.

**Q: How do I configure environment variables?**
A: Create a `.env` file (add to `.gitignore` automatically). Load with `python-dotenv` package if needed.

### REST API

**Q: How do I start the FastAPI server?**
A: Run `python main.py` or `make api`. Server starts at http://localhost:8000

**Q: How do I access the API documentation?**
A: Visit http://localhost:8000/docs for Swagger UI or http://localhost:8000/redoc for ReDoc

**Q: Can I use the API from other programming languages?**
A: Yes! The API is RESTful and language-agnostic. Use any HTTP client (requests in Python, fetch in JavaScript, curl in bash, etc.)

**Q: What's the maximum data size the API can handle?**
A: Default is 10MB per request. Heatmaps are limited to 1000x1000 cells for performance.

**Q: How do I download a generated heatmap?**
A: Use `POST /api/v1/heatmap/download` which returns a 300 DPI PNG file. See API examples for details.

**Q: Can the API handle concurrent requests?**
A: Yes, Uvicorn supports concurrent requests. Performance depends on your server resources.

**Q: How do I deploy the API to production?**
A: Build Docker image with `make docker-build`, or deploy with Uvicorn: `uvicorn src.api:app --host 0.0.0.0 --port 8000`

**Q: Does the API require authentication?**
A: Not currently. For production, add authentication middleware (OAuth2, JWT, API keys, etc.) as needed.

**Q: How do I add custom endpoints to the API?**
A: Edit `src/api.py` and add new routes. Follow the existing patterns for consistency. Don't forget tests!

**Q: Can I use the API without starting the server?**
A: Yes, import the modules directly: `from src import HeatmapVisualizer, MetricsProcessor`

### Troubleshooting

**Q: Tests are failing. How do I debug?**
A: Run `pytest -v` for verbose output, or use `pytest --pdb` to drop into debugger on failure.

**Q: Code Review Agent isn't working. What's wrong?**
A: Ensure `code_review.py` is in the project root. Run manually with `python code_review.py` to see errors.

**Q: GitHub Actions failing but local checks pass?**
A: Different Python versions might behave differently. Check the Actions log and run tests with all supported Python versions locally.

---

## 🎓 Design Principles & Architecture Decisions

### Why Python?
- **Enterprise-Ready**: Mature ecosystem with extensive libraries
- **Data Science**: Native support for data processing (Pandas, NumPy)
- **Type Safety**: Modern type hints enable static analysis
- **Community**: Large community and abundant resources
- **Productivity**: Fast development cycles with minimal boilerplate

### Why These Guardrails?
- **Black**: Eliminates formatting debates with automatic, opinionated formatting
- **MyPy**: Catches type errors before runtime, improving reliability
- **Pytest**: Industry-standard testing framework with excellent plugins
- **Pre-commit**: Shift-left approach catches issues before repository pollution
- **CodeReview Agent**: Automated pattern analysis scales code review effectiveness

### Why Docker?
- **Reproducibility**: "It works on my machine" problem solved
- **Isolation**: Dependencies don't interfere with system packages
- **Scalability**: Easy deployment to cloud platforms
- **CI/CD**: Native support in GitHub Actions
- **Development**: Containers enable consistent dev environments

### Why Seaborn for Visualization?
- **Publication-Quality**: Professional-looking output by default
- **Built on Matplotlib**: Full customization available
- **Statistical Focus**: Designed for business metrics and analytics
- **Integration**: Works seamlessly with Pandas DataFrames
- **Community**: Well-documented with extensive examples

### Why Strict Type Checking?
- **Early Error Detection**: Catches bugs during development
- **Code Documentation**: Types serve as inline documentation
- **IDE Support**: Enables advanced IDE features (autocomplete, refactoring)
- **Maintainability**: Reduces cognitive load for future developers
- **Refactoring Safety**: Large changes are safer with type checking

### Why 80% Coverage Minimum?
- **Risk Mitigation**: Untested code is risky code
- **Regression Prevention**: Coverage catches unintended side effects
- **Confidence**: High coverage enables aggressive refactoring
- **Industry Standard**: Aligns with enterprise practices
- **Balanced Approach**: Not too strict (100%) but meaningful (>75%)

---

## GitHub Actions Workflow

Automated CI/CD pipeline (`python-guardrails.yml`) that:

1. **Lint & Test** (Matrix: Python 3.9, 3.10, 3.11)
   - Runs pre-commit hooks
   - Type checking with MyPy
   - Security scanning with Bandit
   - Dependency vulnerability check
   - CodeReview Agent analysis
   - Unit tests with coverage reporting

2. **Code Quality**
   - Pylint analysis
   - Flake8 style check
   - Black formatting check

## CodeReview Agent

The CodeReview Agent (`code_review.py`) performs automated code quality analysis before pushing to GitHub:

### Checks Performed

1. **Docstring Validation**
   - Detects missing docstrings in functions and classes
   - Reports on every public function/class
   - Examples: "Function 'xyz' missing docstring"

2. **Type Hints Verification**
   - Checks for missing return type hints
   - Checks for missing argument type hints
   - Flags functions without proper type annotations

3. **Magic Numbers Detection**
   - Identifies hardcoded numeric constants in code
   - Suggests converting to named constants
   - Allows common values (0, 1, -1, 2, 100)

4. **Complexity Analysis**
   - Calculates cyclomatic complexity
   - Flags high-complexity functions (>10)
   - Warns on moderate complexity (>7)
   - Suggests refactoring opportunities

5. **Unused Variable Detection**
   - Identifies potentially unused variables
   - Reports on assignments without usage

### Usage

```bash
# Run code review on entire src directory
python code_review.py

# Run code review on specific files
python code_review.py src/module.py src/another_module.py

# Via Makefile
make code-review

# As pre-commit hook (automatic before commits)
pre-commit install
```

### Output Example

```
======================================================================
CODE REVIEW REPORT
======================================================================

Total Files Reviewed: 2
✓ Passed: 1
⚠ Warnings: 1
✗ Failed: 0

Total Issues Found: 0
Total Warnings: 3

----------------------------------------------------------------------
FILE DETAILS
----------------------------------------------------------------------

✓ src/__init__.py
  Warnings:
    • Function 'create_heatmap' has moderate complexity (8) (line 45)
    • Argument 'fmt' missing type hint (line 48)
    • Variable 'temp_fig' may be unused (line 52)

======================================================================
```

### Integration with GitHub

The CodeReview Agent runs automatically in GitHub Actions before allowing merges:
- Reviews all Python files in the push
- Fails on critical issues
- Warns on best practice violations
- Required status check for PRs

## Example: Creating a Heatmap

```python
import pandas as pd
import numpy as np
from src import HeatmapVisualizer, MetricsProcessor

# Create sample data
data = pd.DataFrame(np.random.randn(5, 5), 
                   columns=['A', 'B', 'C', 'D', 'E'])

# Process data
processor = MetricsProcessor()
processor.load_data(data)

# Create visualization
visualizer = HeatmapVisualizer(figsize=(10, 8))
fig = visualizer.create_heatmap(data, title="My Heatmap")
visualizer.save_figure(fig, "output.png")
```

## Configuration Files

### pyproject.toml
Central configuration file containing:
- Project metadata
- Dependencies and optional dependencies
- Tool configurations (black, mypy, pytest, pylint, isort, bandit)

### .pre-commit-config.yaml
Automated code quality checks before commits:
- Trailing whitespace
- YAML validation
- JSON validation
- Private key detection
- Black formatting
- isort import sorting
- Flake8 linting
- MyPy type checking
- Bandit security scanning

## Performance Considerations

- Coverage threshold: 80% minimum
- Type hints required (MyPy strict mode)
- Line length: 100 characters
- Python version support: 3.9+

## Contributing

1. Create a feature branch
2. Make changes (pre-commit hooks will validate, including CodeReview Agent)
3. Write tests (maintain >80% coverage)
4. Push to branch
5. Create Pull Request (GitHub Actions will run full CI/CD including code review)

The CodeReview Agent will run as a pre-commit hook automatically, flagging any issues before you push code to GitHub.

---

## 📌 Scope Limitations

### Current Scope
- **Data Visualization**: Limited to 2D heatmaps via Seaborn
- **Data Sources**: File-based (CSV, JSON) or in-memory DataFrames
- **Python Versions**: 3.9, 3.10, 3.11 (3.12+ not yet tested)
- **Operating Systems**: Linux, macOS, Windows (with Python installed)
- **Deployment**: Docker and manual setup only

### Out of Scope
- Real-time data streaming
- Multi-dimensional interactive visualizations
- User authentication and authorization
- Database connectivity (direct integration)
- Mobile application support
- Kubernetes orchestration (Docker only)

### Known Limitations
- Heatmaps limited to 1000x1000 cells for performance
- Single-threaded execution (no async support)
- In-memory data processing only (no distributed computing)
- CodeReview Agent uses static analysis only (no runtime analysis)
- Type checking requires Python 3.9+ for advanced features

---

## 🚀 Future Enhancements (Roadmap)

### Phase 1.5 (Completed ✅)
- [x] REST API endpoints for metrics & visualization (FastAPI)
- [x] CodeReview Agent for automated code analysis
- [x] GitHub Actions CI/CD pipeline
- [x] Comprehensive guardrails (Black, MyPy, Pytest, Bandit, etc.)

### Phase 2 (Q3 2026)
- [ ] Database integration (PostgreSQL, MongoDB)
- [ ] Advanced visualization types (3D plots, interactive charts)
- [ ] Web UI dashboard
- [ ] Multi-threading support
- [ ] Real-time metrics streaming support
- [ ] API authentication (OAuth2, JWT)

### Phase 3 (Q4 2026)
- [ ] Machine learning model integration
- [ ] Anomaly detection capabilities
- [ ] Predictive analytics
- [ ] Historical data trending
- [ ] Alert and notification system
- [ ] Kubernetes deployment templates

### Phase 4 (2027)
- [ ] Distributed computing support
- [ ] Cloud platform integration (AWS, Azure, GCP)
- [ ] Enterprise authentication (SSO, LDAP)
- [ ] Advanced security features (encryption, audit logs)
- [ ] Performance optimization for large datasets (>10M rows)

### Continuous Improvements
- [ ] Python 3.12+ support
- [ ] Expand CodeReview Agent capabilities
- [ ] Enhanced test coverage (target >95%)
- [ ] Performance benchmarking suite
- [ ] Documentation improvements

---

## License

MIT

## Support

For issues or questions, refer to the GitHub Actions logs or run local guardrails checks:

```bash
# Quick validation before pushing
pre-commit run --all-files && python code_review.py && pytest tests/ && mypy src/
```

Or use the Makefile for comprehensive checks:

```bash
make all
```

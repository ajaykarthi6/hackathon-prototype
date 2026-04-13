# Interstellar Agent ADK

A clean GitHub repository scaffold for an interstellar education agent built with Python, FastAPI, and deployment automation.

## Repository structure

- `.github/workflows/` - GitHub Actions workflows for CI and deployment
- `src/` - Python application source code
- `tests/` - Unit and integration tests
- `infrastructure/terraform/` - Terraform configuration for cloud deployment
- `Dockerfile` - Container image build instructions
- `requirements.txt` - Python dependencies
- `.env.example` - Example environment configuration
- `LICENSE` - Source code license

## Getting started

1. Clone the repository.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the API locally:
   ```bash
   uvicorn src.api.main:app --reload
   ```
4. Run tests:
   ```bash
   pytest -q
   ```

## Notes

This repository is organized for a clean GitHub experience with a clear project layout, CI automation, and deployment scaffolding.

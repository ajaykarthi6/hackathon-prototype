# Interstellar Agent ADK

A GitHub-ready Python project scaffold for an interstellar education agent. This repository includes a minimal FastAPI backend, test coverage, CI/CD workflows, Docker packaging, and Terraform deployment placeholders.

## Features

- FastAPI-based HTTP API with a `/query` endpoint
- Basic agent logic and prompt configuration
- Unit and integration test examples with `pytest`
- GitHub Actions workflows for CI and deployment
- Dockerfile for containerization
- Terraform placeholders for cloud infrastructure

## Repository structure

- `.github/workflows/` - CI/CD workflows for GitHub Actions
- `src/` - Python application source code
- `tests/` - Test suite for app logic and API integration
- `infrastructure/terraform/` - Terraform config for cloud deployment
- `Dockerfile` - Docker image build instructions
- `requirements.txt` - Python dependencies
- `.env.example` - Environment variable examples
- `LICENSE` - Project license

## Quick start

```bash
git clone https://github.com/ajaykarthi6/hackathon-prototype.git
cd hackathon-prototype
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run locally

```bash
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
```

Then visit `http://localhost:8000/docs` for the OpenAPI UI.

### Example request

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Tell me about Mars"}'
```

## Run tests

```bash
pytest -q
```

## Contribution

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and add tests.
4. Commit your work: `git commit -m "Add feature description"`
5. Push to your fork: `git push origin feature/your-feature`
6. Open a pull request against `main`.

## Notes

- The current implementation is scaffolded with placeholder logic. Extend `src/agent/logic.py`, `src/tools/wikipedia_grounding.py`, and `src/api/schemas.py` to add real functionality.
- Configure CI/CD secrets before using the `.github/workflows/cd-deploy.yml` workflow.

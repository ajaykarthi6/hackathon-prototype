# Interstellar Agent ADK

A GitHub-ready Python project scaffold for an interstellar education agent. This repository includes a minimal FastAPI backend with a web UI, test coverage, CI/CD workflows, Docker packaging, and Terraform deployment placeholders.

## Project Overview

The **Interstellar Agent ADK (Agent Development Kit)** is an innovative educational platform designed to provide interactive, AI-powered insights about our solar system's planets. Built as a hackathon prototype, this project demonstrates modern web development practices, API design, and deployment automation.

### Core Concept
Imagine an intelligent agent that travels through space, collecting and sharing knowledge about celestial bodies. The Interstellar Agent acts as your personal guide to planetary science, offering detailed information about Mars, Venus, Jupiter, and potentially other planets in our solar system.

### Key Components

#### 🤖 Agent Logic (`src/agent/`)
- **Dynamic Response System**: Matches user queries to planetary data using intelligent keyword detection
- **Extensible Data Model**: Planet information stored in structured dictionaries for easy expansion
- **Prompt Engineering**: Configurable system prompts to maintain educational focus

#### 🌐 Web Interface (`templates/`)
- **User-Friendly UI**: Clean, responsive HTML interface with real-time query responses
- **No-Code Interaction**: Users can explore planetary data without technical knowledge
- **Visual Feedback**: Styled responses with proper formatting for data presentation

#### 🔌 API Layer (`src/api/`)
- **RESTful Endpoints**: JSON API for programmatic access (`/query`)
- **Web Form Handling**: HTML form processing (`/web-query`) for seamless integration
- **FastAPI Framework**: High-performance async web framework with automatic OpenAPI docs

#### 🧪 Testing Suite (`tests/`)
- **Unit Tests**: Validate agent logic for each planet
- **Integration Tests**: Ensure API endpoints work correctly
- **Comprehensive Coverage**: Tests for known planets and unknown queries

#### 🚀 DevOps & Deployment
- **CI/CD Pipelines**: Automated testing and deployment via GitHub Actions
- **Containerization**: Docker support for consistent environments
- **Infrastructure as Code**: Terraform templates for cloud deployment
- **Environment Management**: Configurable settings via environment variables

### Technical Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Browser   │────│   FastAPI App   │────│   Agent Logic   │
│                 │    │                 │    │                 │
│  HTML Interface │    │  /query (JSON)  │    │ Planetary Data  │
│  Form Submission│    │ /web-query (HTML│    │ Response Builder│
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   Planet Data   │
                    │   Dictionary    │
                    └─────────────────┘
```

### Educational Value
This project serves as both a functional tool and a learning resource:
- **API Design**: Demonstrates RESTful API best practices
- **Web Development**: Shows integration of backend and frontend
- **Testing**: Illustrates comprehensive test coverage
- **DevOps**: Provides examples of CI/CD and containerization
- **Python Best Practices**: Clean code structure and modern libraries

### Future Enhancements
- Integration with real astronomical APIs (NASA, ESA)
- AI-powered natural language processing for complex queries
- Interactive visualizations and 3D models
- Multi-language support
- User authentication and personalized learning paths

## Features

- **Multi-Planet Support**: Ask about Mars, Venus, or Jupiter for detailed responses.
- **Web Interface**: Interactive web UI for easy querying.
- **API Endpoints**: JSON API for programmatic access.
- **Comprehensive Testing**: Unit and integration tests.
- **CI/CD Ready**: Automated testing and deployment pipelines.
- **Containerized**: Docker support for easy deployment.

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

Then visit `http://localhost:8000` for the web UI or `http://localhost:8000/docs` for the OpenAPI UI.

### Example request

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Tell me about Mars"}'
```

Or use the web interface at `http://localhost:8000`.

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

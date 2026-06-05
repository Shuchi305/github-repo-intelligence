# GitHub Repo Intelligence

AI-powered platform to help developers understand unfamiliar GitHub repositories by combining deterministic code analysis (framework detection, symbol indexing, dependency graphs) with targeted LLM calls to generate onboarding guides and evidence-backed Q&A.

Getting started

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the basic entrypoint:

```bash
python main.py
```

Project structure

- `app/` — backend application modules (framework detection, scanners, AI, storage).
- `docs/` — project specification and API/architecture docs.
- `tests/` — placeholder tests.
- `repos/` — cloned repositories for analysis.

Documentation

- Design and pipeline: `docs/project-spec.md`
- Architecture: `docs/architecture.md`
- API surface: `docs/api-design.md`

Next steps

- Run tests: `pytest` (tests are currently placeholders).
- Implement API wiring and background job handling for long-running analyses.

License

This repository does not include a license file yet.
GitHub Repo Intelligence Platform  AI-powered onboarding and repository understanding tool

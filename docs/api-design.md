# API Design

This document outlines the initial backend API surface for repository analysis, onboarding guide generation, and Q&A.

Base URL: `/` (served by FastAPI)

Endpoints

- `GET /health` — simple health check.
	- Response: `200 OK` with `{ "status": "ok" }`.

- `POST /analyze` — analyze a repository.
	- Request body: `{ "repo_url": "https://github.com/owner/repo" }`
	- Response: 200 with an `analysis` object (RepositoryContext summary) or a job id if run asynchronously.

- `GET /analysis/{id}` — retrieve analysis results by id.
	- Response: analysis summary including frameworks, languages, symbol counts, dependency graph metadata, and evidence references.

- `GET /onboarding/{id}` — get the generated onboarding guide for a repository.

- `POST /qa` — ask a question about an analyzed repository.
	- Request body: `{ "analysis_id": "...", "question": "How does authentication work?" }`
	- Response: answer with evidence-backed citations (files, snippets, and locations).

Schemas

- HealthResponse: use `HealthResponse` in `app/api/schemas.py` for health endpoint responses.

Notes

- Endpoints may be implemented synchronously for small repos and asynchronously for large analyses (job queue + polling).
- All AI-generated outputs must include evidence (file paths, code snippets, and dependency traces) to satisfy the design principle of explainability.

Security

- For V1, API is unauthenticated; plan for API keys and rate limiting in future iterations.

See `docs/project-spec.md` for pipeline stages and expected analysis contents.

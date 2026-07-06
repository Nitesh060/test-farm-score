# Farm Credit Platform

A full-stack platform for farm suitability scoring and credit assessment,
combining satellite data, geospatial boundaries, and ML-based scoring
with a FastAPI backend and React frontend.

## Structure

- `backend/` — FastAPI application (API, services, ML models, DB layer)
- `frontend/` — React + TypeScript client
- `database/` — SQL schema and seed data
- `docs/` — Architecture docs, API exports, runbooks
- `scripts/` — Dev environment setup and deployment scripts
- `tests/e2e/` — End-to-end tests
- `.github/workflows/` — CI/CD pipelines

## Getting Started

```bash
./scripts/setup_dev_env.sh
docker-compose up -d
```

Backend runs at `http://localhost:8000`, frontend at `http://localhost:3000`.

## License

TBD

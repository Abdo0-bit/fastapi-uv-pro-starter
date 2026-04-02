# FastAPI Pro Starter

> **"Built by a Backend Developer for Backend Developers. No fluff, just structure."**

A professional, scalable FastAPI boilerplate focused on clean architecture, maintainability, and production-friendly defaults.

## Key Features

- uv-first dependency and environment management via pyproject.toml and uv.lock.
- Strong configuration management with pydantic-settings and .env mapping.
- API versioning structure using app/api/v1 for clean endpoint evolution.
- yped request/response contracts with Pydantic schemas.
- Health check endpoint ready at /api/v1/health.

## Project Layout

```text
app/
  api/
    v1/
      endpoints/
        health.py
      router.py
  core/
    config.py
  models/
    base.py
  schemas/
    health.py
  main.py
```

## 🛠️ Setup (uv)

### Windows (PowerShell)

1. Copy environment values.

```powershell
Copy-Item .env.example .env
```

2. Sync dependencies.

```powershell
uv sync
```

3. Run development server.

```powershell
uv run uvicorn app.main:app --reload
```

### Linux and macOS (bash/zsh)

1. Copy environment values.

```bash
cp .env.example .env
```

2. Sync dependencies.

```bash
uv sync
```

3. Run development server.

```bash
uv run uvicorn app.main:app --reload
```

## API Docs

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Health Endpoint

- GET /api/v1/health

Example response:

```json
{
  "status": "ok",
  "app_name": "FastAPI Pro Starter",
  "debug": false,
  "environment": "development",
  "timestamp_utc": "2026-04-02T12:00:00+00:00"
}
```

## Environment Variables

- APP_NAME: Service title shown in OpenAPI docs.
- APP_VERSION: Service version used by FastAPI metadata.
- DEBUG: Enables debug mode when true.
- API_V1_PREFIX: Prefix for all version 1 routes.
- ENVIRONMENT: One of development, staging, or production.

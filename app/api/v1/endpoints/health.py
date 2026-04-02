from datetime import datetime, timezone

from fastapi import APIRouter

from app.core.config import get_settings
from app.schemas.health import HealthResponse

router: APIRouter = APIRouter(prefix="/health")


@router.get("", response_model=HealthResponse, summary="Health check")
def health_check() -> HealthResponse:
    settings = get_settings()
    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        debug=settings.debug,
        environment=settings.environment,
        timestamp_utc=datetime.now(timezone.utc),
    )

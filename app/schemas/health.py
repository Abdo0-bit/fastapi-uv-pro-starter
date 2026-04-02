from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: Literal["ok"] = Field(
        default="ok",
        description="Service health status.",
    )
    app_name: str = Field(description="Configured application name.")
    debug: bool = Field(description="Whether debug mode is enabled.")
    environment: str = Field(description="Runtime environment label.")
    timestamp_utc: datetime = Field(description="UTC response timestamp.")

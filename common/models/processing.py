from typing import List
from pydantic import BaseModel, Field

from api.common.models.point import Point


class ProcessingResult(BaseModel):
    points: List[Point] = Field(
        ..., description="Processed points", example=[Point]
    )

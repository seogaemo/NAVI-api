from typing import List
from pydantic import BaseModel, Field

from api.common.dto.pedestrian.response import PedestrianRouteResponse
from api.common.models.point import Point


class ProcessingResult(BaseModel):
    walkablityIndex: float = Field(
        ..., description="Walkablity index", example=0.5
    )

    labelCount: List[int] = Field(
        ..., description="각 라벨의 개수", example=[1, 2, 3]
    )

    points: List[Point] = Field(..., description="Processed points")

    time: int = Field(..., description="Time to reach destination (seconds)")

    distance: int = Field(
        ..., description="Distance to reach destination (meters)"
    )

    road: PedestrianRouteResponse = Field(
        ...,
        description="Pedestrian route response",
    )


class ProcessingMultiResult(BaseModel):
    suggestion: ProcessingResult = Field(
        ..., description="Suggestion route (추천 경로)"
    )

    boulevard: ProcessingResult = Field(
        ..., description="Boulevard route (대로 우선)"
    )

    shortest: ProcessingResult = Field(
        ..., description="Shortest route (최단 + 계단 제외 경로)"
    )

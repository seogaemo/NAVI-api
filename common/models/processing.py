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

    road: PedestrianRouteResponse = Field(
        ...,
        description="Pedestrian route response",
    )


class ProcessingMultiResult(BaseModel):
    results: List[ProcessingResult] = Field(
        ..., description="Processed results"
    )
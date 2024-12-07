from typing import List
from pydantic import BaseModel, Field


class LineString(BaseModel):
    x: List[float] = Field(
        ...,
        description="x 좌표 리스트",
        example=[127.032061691553, 127.032095359532],
    )
    y: List[float] = Field(
        ...,
        description="y 좌표 리스트",
        example=[37.2781204926811, 37.2781189700618],
    )
    count: int = Field(..., description="좌표 개수", example=2)
    distance: float = Field(..., description="총 거리 (m)", example=3000)
    time: float = Field(..., description="총 소요시간 (초)", example=600)

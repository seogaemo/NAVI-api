from pydantic import BaseModel, Field

from api.common.dto.pedestrian.response import PedestrianRouteResponse

from api.common.models.processing import ProcessingResult


class PedestrianRoute(BaseModel):
    original: PedestrianRouteResponse = Field(
        ..., description="Original pedestrian route information"
    )
    result: ProcessingResult = Field(
        ..., description="Processed pedestrian route information"
    )

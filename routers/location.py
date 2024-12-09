from fastapi import APIRouter

from api.common.models.point import Point, PointWithDistance
from api.services.location.location_service import Location


router = APIRouter(prefix="/location", tags=["Location"])
location = Location()


@router.get("/point")
async def get_nearby_points(
    x: float, y: float, limit: int = 10
) -> list[PointWithDistance]:
    """
    # 주변 포인트 조회 API

    주변 포인트 정보를 조회하는 함수입니다.
    """

    return await location.getManyPoints(x, y, limit)

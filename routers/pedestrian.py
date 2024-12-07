from fastapi import APIRouter

from api.services.main.main_service import MainService
from api.common.dto.pedestrian.request import PedestrianRouteRequest

router = APIRouter(prefix="/pedestrian")

main = MainService()


@router.post("/")
async def getPedestrianRoute(data: PedestrianRouteRequest):
    """
    보행자 경로 안내 API를 호출하여 경로 정보를 반환하는 함수입니다.
    """

    return await main.getPedestrianRoute(data)

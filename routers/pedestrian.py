from fastapi import APIRouter

from api.common.models.processing import ProcessingMultiResult, ProcessingResult
from api.services.main.main_service import MainService
from api.common.dto.pedestrian.request import PedestrianRouteRequest

router = APIRouter(prefix="/pedestrian", tags=["Pedestrian"])

main = MainService()


@router.post("/single")
async def get_single_pedestrian_route(
    data: PedestrianRouteRequest,
) -> ProcessingResult:
    """
    # 보행자 경로 안내 API (단일 버전)

    보행자 경로 안내 API를 호출하여 경로 정보를 반환하는 함수입니다.

    https://openapi.sk.com/products/detail?svcSeq=4&menuSeq=45
    """

    return await main.getPedestrianRoute(data)


@router.post("/multi")
async def get_multi_pedestrian_route(
    data: PedestrianRouteRequest,
) -> ProcessingMultiResult:
    """
    # 보행자 경로 안내 API (다중 버전)

    보행자 경로 안내 API를 호출하여 경로 정보를 반환하는 함수입니다.

    총 3개의 경로를 반환합니다.

    https://openapi.sk.com/products/detail?svcSeq=4&menuSeq=45
    """

    return await main.getMultiPedestrianRoute(data)

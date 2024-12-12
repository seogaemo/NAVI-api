from fastapi import APIRouter, Depends

from api.common.dto.pedestrian.request import PedestrianRouteRequest
from api.common.dto.poi.request import SearchParams
from api.common.dto.poi.response import PoiResponse
from api.services.poi.poi_service import Poi

router = APIRouter(prefix="/poi", tags=["Poi"])

poi = Poi()

async def getSearchParams(
    search_params: SearchParams = Depends(),
) -> SearchParams:
    return search_params

@router.get("/search")
async def search_poi(
    params: SearchParams = Depends(getSearchParams)
) -> PoiResponse:
    """
    # 장소(POI) 검색 API

    Tmap POI 검색 API를 사용하여 장소를 검색합니다.
    """

    return await poi.search(params)
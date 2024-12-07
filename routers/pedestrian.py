from fastapi import APIRouter

from api.services.pedestrian.pedestrian_service import SKPedestrian
from api.common.dto.pedestrian.request import PedestrianRouteRequest

router = APIRouter(prefix="/pedestrian")


@router.post("/")
async def getPedestrianRoute(data: PedestrianRouteRequest):
    pedestrian = SKPedestrian()
    route = await pedestrian.getPedestrianRoute(data)
    lineString = await pedestrian.extractLineString(route)

from fastapi import APIRouter

from api.services.location.location_service import Location
from api.services.pedestrian.pedestrian_service import SKPedestrian
from api.common.dto.pedestrian.request import PedestrianRouteRequest

router = APIRouter(prefix="/pedestrian")


@router.post("/")
async def getPedestrianRoute(data: PedestrianRouteRequest):
    pedestrian = SKPedestrian()
    location = Location()

    route = await pedestrian.getPedestrianRoute(data)
    lineString = await pedestrian.extractLineString(route)

    points = await location.getPoints(
        lineString.y, lineString.x, lineString.count
    )

    return {"points": points}

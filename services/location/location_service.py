from api.common.models.point import Point
from api.common.utils.db import DB


class Location:
    def __init__(self):
        self.db = DB()

    async def getPoints(
        self, lat: list[float], lng: list[float], count: int
    ) -> list[Point]:
        points = []

        for i in range(count):
            point = await self.getPoint(lat[i], lng[i])

            if point is not None:
                points.append(point)

        return points

    async def getPoint(self, lat: float, lng: float) -> Point | None:
        rows = self.db.getNearestLocations(lat, lng, limit=1)

        if rows is None:
            return None

        for row in rows:
            return Point(
                id=row[0],
                lat=row[1],
                lng=row[2],
                ele=row[3],
                time=row[4].isoformat(),
                duration=row[5],
                speed=row[6],
                video=row[7],
            )

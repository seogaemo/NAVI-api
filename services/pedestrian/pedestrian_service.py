import requests
from pydantic import TypeAdapter

from api.common.utils.config import Settings

from api.common.models.line import LineString

from api.common.dto.pedestrian.request import PedestrianRouteRequest
from api.common.dto.pedestrian.response import PedestrianRouteResponse


class SKPedestrian:
    def __init__(self):
        self.settings = Settings()

    async def extractLineString(
        self, route: PedestrianRouteResponse
    ) -> LineString:
        lineString = LineString(x=[], y=[], count=0, distance=0, time=0)

        for feature in route.features:
            if feature.properties.pointType == "SP":
                lineString.x.append(feature.geometry.coordinates[0])
                lineString.y.append(feature.geometry.coordinates[1])
                lineString.count += 1
                lineString.distance = feature.properties.totalDistance
                lineString.time = feature.properties.totalTime

            if feature.geometry.type == "LineString":
                for coordinate in feature.geometry.coordinates:
                    if coordinate == [lineString.x[-1], lineString.y[-1]]:
                        continue

                    lineString.x.append(coordinate[0])
                    lineString.y.append(coordinate[1])
                    lineString.count += 1

        return lineString

    async def getPedestrianRoute(
        self, data: PedestrianRouteRequest
    ) -> PedestrianRouteResponse:
        """
        Tmap 보행자 경로 안내 API를 호출하여 경로 정보를 반환하는 함수입니다.

        Args:
            data: PedestrianRouteRequest DTO

        Returns:
            PedestrianRouteResponse: 보행자 경로 안내 응답 정보를 담은 DTO 객체

        Raises:
            requests.exceptions.RequestException: API 요청 실패 시 발생하는 예외
        """

        url = "https://apis.openapi.sk.com/tmap/routes/pedestrian"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "appKey": self.settings.SK_APPKEY,
        }

        params = {
            "version": 1,
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                params=params,
                json=data.model_dump(exclude_none=True),
            )

            if response.status_code != 200:
                print(f"SK Pedestrian API Request Failed: {response.text}")
                raise requests.exceptions.RequestException

            adapter = TypeAdapter(PedestrianRouteResponse)
            return adapter.validate_python(response.json())

        except requests.exceptions.RequestException as e:
            print(f"SK Pedestrian API Request Failed: {e}")
            raise

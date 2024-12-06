import requests
from pydantic import TypeAdapter

from api.common.utils.config import Settings

from .dtos.request import PedestrianRouteRequest
from .dtos.response import PedestrianRouteResponse


class SKPedestrian():
    def __init__(self):
        self.settings = Settings()

    async def getRoute(
        self,
        data: PedestrianRouteRequest
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
            response = requests.post(url, headers=headers, params=params, json=data.model_dump())
            response.raise_for_status()
            adapter = TypeAdapter(PedestrianRouteResponse)
            return adapter.validate_python(response.json())

        except requests.exceptions.RequestException as e:
            print(f"SK Pedestrian API Request Failed: {e}")
            raise
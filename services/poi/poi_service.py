from pydantic import TypeAdapter
import requests
from api.common.dto.poi.request import SearchParams
from api.common.dto.poi.response import PoiResponse
from api.common.utils.config import Settings


class Poi:
    def __init__(self):
        self.settings = Settings()
        pass

    async def search(self, params: SearchParams):
        """
        Tmap POI 검색 API를 사용하여 장소를 검색합니다.
        """
        
        url = "https://apis.openapi.sk.com/tmap/pois"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "appKey": self.settings.SK_APPKEY,
        }

        try:
            response = requests.get(
                url,
                headers=headers,
                params=params.model_dump(),
            )

            if response.status_code != 200:
                print(f"SK Poi Search API Request Failed: {response.text}")
                raise requests.exceptions.RequestException

            adapter = TypeAdapter(PoiResponse)
            return adapter.validate_python(response.json())

        except requests.exceptions.RequestException as e:
            print(f"SK Poi Search API Request Failed: {e}")
            raise
from io import BytesIO
from fastapi.responses import StreamingResponse
import requests

from api.common.utils.config import Settings


class Image:
    def __init__(self):
        self.settings = Settings()

    def getImage(self, pointId: str) -> StreamingResponse:
        """
        이미지를 반환하는 함수입니다.

        FastAPI의 StreamingResponse로 반환합니다.
        """

        try:
            response = requests.get(f"{self.settings.S3_URL}/{pointId}.jpg")

            if response.status_code != 200:
                print(f"Image API Request Failed: {response.text}")
                raise requests.exceptions.RequestException

            return StreamingResponse(
                BytesIO(response.content), media_type="image/jpeg"
            )

        except requests.exceptions.RequestException as e:
            return None

    def getPredictedImage(self, pointId: str) -> StreamingResponse:
        """
        예측된 이미지를 반환하는 함수입니다.

        FastAPI의 StreamingResponse로 반환합니다.
        """

        try:
            response = requests.get(
                f"{self.settings.PREDICTION_URL}/image?id={pointId}"
            )

            if response.status_code != 200:
                print(f"Image API Request Failed: {response.text}")
                raise requests.exceptions.RequestException

            return StreamingResponse(
                BytesIO(response.content), media_type="image/jpeg"
            )

        except requests.exceptions.RequestException as e:
            return None

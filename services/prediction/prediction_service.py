import requests
from pydantic import TypeAdapter

from api.common.dto.prediction.response import PredictionResponse
from api.common.models.object import PredictionObject
from api.common.utils.config import Settings
from api.common.utils.db import DB


class Prediction:
    def __init__(self):
        self.settings = Settings()
        self.db = DB()

    async def getPredtions(self, pointIds: list[str]) -> list[PredictionObject]:
        """
        예측 결과를 반환하는 함수입니다.
        """

        predictions = []

        for pointId in pointIds:
            prediction = await self.getPrediction(pointId)

            if prediction is not None:
                predictions.extend(prediction.predictions)

        return PredictionResponse(predictions=predictions).predictions

    async def getPrediction(self, pointId: str) -> PredictionResponse:
        """
        예측 결과를 반환하는 함수입니다.
        """

        prediction = await self.getPredictionFromDB(pointId)

        if prediction is not None:
            return prediction

        try:
            response = requests.get(
                f"{self.settings.PREDICTION_URL}?id={pointId}"
            )

            if response.status_code != 200:
                print(f"Prediction API Request Failed: {response.text}")
                raise requests.exceptions.RequestException

            adapter = TypeAdapter(PredictionResponse)
            prediction = adapter.validate_python(response.json())

            await self.savePredictionToDB(pointId, prediction)

            return prediction
        except requests.exceptions.RequestException as e:
            print(f"Prediction API Request Failed: {e}")
            raise

    async def getPredictionFromDB(self, pointId: str) -> PredictionResponse:
        """
        DB에 캐싱된 예측 결과를 반환하는 함수입니다.
        """

        return self.db.getPrediction(pointId)

    async def savePredictionToDB(
        self, pointId: str, predictions: PredictionResponse
    ):
        """
        DB에 예측 결과를 저장하는 함수입니다.
        """

        return self.db.savePrediction(pointId, predictions)

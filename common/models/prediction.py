from pydantic import BaseModel, Field


class PredictionResult(BaseModel):
    """
    Prediction 결과를 담는 DTO입니다.
    """

    labelCount: list[int] = Field(
        None, description="각 라벨의 개수", example=[1, 2, 3]
    )

from typing import List
from pydantic import BaseModel

from api.common.models.object import PredictionObject


class PredictionResponse(BaseModel):
    predictions: List[PredictionObject]

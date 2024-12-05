from typing import List
from pydantic import BaseModel


class PredictionResult(BaseModel):
    xmin: int
    ymin: int
    xmax: int
    ymax: int
    label: int
    confidence: float


class PredictionResults(BaseModel):
    predictions: List[PredictionResult]

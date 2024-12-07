from pydantic import BaseModel


class PredictionObject(BaseModel):
    xmin: int
    ymin: int
    xmax: int
    ymax: int
    label: int
    confidence: float

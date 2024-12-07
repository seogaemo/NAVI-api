from api.common.constants.label import LABELS
from api.common.constants.weight import WEIGHTS
from api.common.dto.pedestrian.request import PedestrianRouteRequest
from api.common.models.object import PredictionObject
from api.common.models.processing import ProcessingResult
from api.services.location.location_service import Location
from api.services.pedestrian.pedestrian_service import SKPedestrian
from api.services.prediction.prediction_service import Prediction


class MainService:
    def __init__(self):
        self.pedestrian = SKPedestrian()
        self.location = Location()
        self.prediction = Prediction()

    async def getPedestrianRoute(
        self, data: PedestrianRouteRequest
    ) -> ProcessingResult:
        route = await self.pedestrian.getPedestrianRoute(data)
        lineString = await self.pedestrian.extractLineString(route)

        points = await self.location.getPoints(
            lineString.y, lineString.x, lineString.count
        )

        predictions = await self.prediction.getPredtions(
            [point.id for point in points]
        )

        labelCount = await self.getLabelCount(predictions)
        walkabilityIndex = await self.getWalkablityIndex(labelCount)

        return ProcessingResult(
            walkablityIndex=walkabilityIndex,
            labelCount=labelCount,
            points=points,
            road=route,
        )

    async def getWalkablityIndex(self, labelCount: list[int]) -> float:
        walkabilityIndex = 0

        for i in range(len(LABELS)):
            weightOfLabel = 0.1

            try:
                weightOfLabel = WEIGHTS[LABELS[i]]
            except KeyError:
                pass

            walkabilityIndex += labelCount[i] * weightOfLabel

        return walkabilityIndex

    async def getLabelCount(
        self, predictions: list[PredictionObject]
    ) -> list[int]:
        labelCount = [0 for _ in range(len(LABELS))]

        for prediction in predictions:
            labelCount[prediction.label] += 1

        return labelCount

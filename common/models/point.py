from pydantic import BaseModel, Field


class Point(BaseModel):
    """
    road 데이터의 Point 정보를 담는 DTO입니다.
    """

    id: str = Field(None, description="Point ID", example="uuid")
    lat: float = Field(..., description="Latitude", example=37.5665)
    lng: float = Field(..., description="Longitude", example=126.9780)
    ele: float = Field(None, description="Elevation", example=30.0)
    time: str = Field(
        None,
        description="Timestamp",
        example="2024-08-31T11:12:15.254556+00:00",
    )
    duration: float = Field(
        None, description="Duration in seconds", example=120.0
    )
    speed: float = Field(None, description="Speed in m/s", example=5.5)
    video: str = Field(
        None, description="Path to video file", example="/path/to/video.mp4"
    )


class PointWithDistance(Point):
    """
    road 데이터의 Point 정보와 거리 정보를 담는 DTO입니다.
    """

    distance: float = Field(..., description="Distance (km)", example=0.001)

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
        None, description="Timestamp", example="2023-01-01T00:00:00Z"
    )
    duration: float = Field(
        None, description="Duration in seconds", example=120.0
    )
    speed: float = Field(None, description="Speed in m/s", example=5.5)
    video: str = Field(
        None, description="Path to video file", example="/path/to/video.mp4"
    )

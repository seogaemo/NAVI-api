from pydantic import BaseModel, Field


class PedestrianRouteRequest(BaseModel):
    """
    보행자 경로 안내 요청 정보를 담는 DTO입니다.
    """

    # 출발지 및 목적지 정보
    startName: str = Field(
        ...,
        description="출발지 명칭 (UTF-8 URL 인코딩 필수)",
        example=f"SUBWAY%20%ED%95%9C%EC%96%91%EB%8C%80%EC%A0%90",
    )  # URL 인코딩 필수
    startX: float = Field(
        ..., description="출발지 X 좌표 (경도)", example=127.04079334
    )
    startY: float = Field(
        ..., description="출발지 Y 좌표 (위도)", example=37.55881732
    )
    endName: str = Field(
        ...,
        description="목적지 명칭 (UTF-8 URL 인코딩 필수)",
        example=f"%EC%99%95%EC%8B%AD%EB%A6%AC%EC%97%AD%206%EB%B2%88%EC%B6%9C%EA%B5%AC",
    )  # URL 인코딩 필수
    endX: float = Field(
        ..., description="목적지 X 좌표 (경도)", example=127.03923786
    )
    endY: float = Field(
        ..., description="목적지 Y 좌표 (위도)", example=37.56117813
    )
    endPoiId: str = Field(None, description="목적지 POI ID", example="1134301")

    # 경유지 정보
    passList: str = Field(
        None,
        description="경유지의 X, Y 좌표 (최대 5개, '_'로 구분)",
    )
    reqCoordType: str = Field(
        "WGS84GEO",
        description="요청 좌표계 (WGS84GEO, EPSG3857, KATECH)",
        example="WGS84GEO",
    )
    resCoordType: str = Field(
        "WGS84GEO",
        description="응답 좌표계 (WGS84GEO, EPSG3857, KATECH)",
        example="WGS84GEO",
    )

    # 경로 탐색 옵션
    searchOption: int = Field(
        0,
        description="경로 탐색 옵션 (0: 추천, 4: 추천+대로 우선, 10: 최단, 30: 최단거리+계단 제외)",
        example=0,
    )

    # GPS 정보
    angle: int = Field(None, description="각도 (0~359)", example=180)
    speed: int = Field(None, description="진행 속도 (km/h, 0 이상)", example=10)

    # 정렬
    sort: str = Field(
        "index", description="정렬 순서 (index, custom)", example="index"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "startName": f"SUBWAY%20%ED%95%9C%EC%96%91%EB%8C%80%EC%A0%90",
                    "startX": 127.04079334,
                    "startY": 37.55881732,
                    "endName": f"%EC%99%95%EC%8B%AD%EB%A6%AC%EC%97%AD%206%EB%B2%88%EC%B6%9C%EA%B5%AC",
                    "endX": 127.03923786,
                    "endY": 37.56117813,
                    "endPoiId": "1134301",
                    "searchOption": 0,
                }
            ]
        }
    }

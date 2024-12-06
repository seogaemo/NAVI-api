from pydantic import BaseModel, Field

class PedestrianRouteRequest(BaseModel):
    """
    보행자 경로 안내 요청 정보를 담는 DTO입니다.
    """

    # 출발지 및 목적지 정보
    startName: str = Field(..., description="출발지 명칭 (UTF-8 URL 인코딩 필수)", example=f"%EA%B4%91%EC%B9%98%EA%B8%B0%ED%95%B4%EB%B3%80")  # URL 인코딩 필수
    startX: float = Field(..., description="출발지 X 좌표 (경도)", example=126.9246033)
    startY: float = Field(..., description="출발지 Y 좌표 (위도)", example=33.45241976)
    endName: str = Field(..., description="목적지 명칭 (UTF-8 URL 인코딩 필수)", example=f"%EC%98%A8%ED%8F%89%ED%8F%AC%EA%B5%AC")  # URL 인코딩 필수
    endX: float = Field(..., description="목적지 X 좌표 (경도)", example=126.9041895)
    endY: float = Field(..., description="목적지 Y 좌표 (위도)", example=33.4048969)
    endPoiId: str = Field(None, description="목적지 POI ID", example="8932638")

    # 경유지 정보
    passList: str = Field(None, description="경유지의 X, Y 좌표 (최대 5개, '_'로 구분)", example="127.38454163183215,36.35127257501252_127.38668918609662,36.353534038949995")
    reqCoordType: str = Field("WGS84GEO", description="요청 좌표계 (WGS84GEO, EPSG3857, KATECH)", example="WGS84GEO")
    resCoordType: str = Field("WGS84GEO", description="응답 좌표계 (WGS84GEO, EPSG3857, KATECH)", example="WGS84GEO")

    # 경로 탐색 옵션
    searchOption: int = Field(0, description="경로 탐색 옵션 (0: 추천, 4: 추천+대로 우선, 10: 최단, 30: 최단거리+계단 제외)", example=0)

    # GPS 정보
    angle: int = Field(None, description="각도 (0~359)", example=180)
    speed: int = Field(None, description="진행 속도 (km/h, 0 이상)", example=10)

    # 정렬
    sort: str = Field("index", description="정렬 순서 (index, custom)", example="index")

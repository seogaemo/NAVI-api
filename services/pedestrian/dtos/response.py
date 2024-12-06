from pydantic import BaseModel, Field


class PedestrianRouteResponseFeatureProperties(BaseModel):
    """
    보행자 경로 안내 응답의 Feature Properties 정보를 담는 DTO입니다.
    """

    totalDistance: int = Field(None, description="경로 총 거리 (m)", example=3000)
    totalTime: int = Field(None, description="경로 총 소요시간 (초)", example=600)
    index: int = Field(..., description="경로 순번", example=1)
    pointIndex: int = Field(None, description="아이콘 노드", example=1)
    name: str = Field(None, description="안내 지점 명칭", example="SK T 타워")
    description: str = Field(None, description="길 안내 정보", example="소공로 을 따라 소공로 방면으로 310m 이동")
    direction: str = Field(None, description="방면 명칭", example="온평포구")
    nearPoiName: str = Field(None, description="안내 지점 주변 POI 명칭", example="표선해수욕장")
    nearPoiX: float = Field(None, description="안내 지점 주변 POI X 좌표", example=126.83753037)
    nearPoiY: float = Field(None, description="안내 지점 주변 POI Y 좌표", example=33.32787654)
    intersectionName: str = Field(None, description="교차로 명칭", example="신양교차로")
    facilityType: str = Field(None, description="시설물 유형 (1: 교량, 2: 터널, 3: 고가도로, 11: 일반보행자도로, 12: 육교, 14: 지하보도, 15: 횡단보도, 16: 대형시설물이동통로, 17: 계단)", example=1)
    facilityName: str = Field(None, description="시설물 명칭", example="교량")
    turnType: int = Field(None, description="회전 정보 (11: 직진, 12: 좌회전, 13: 우회전, 14: 유턴)", example=14)
    pointType: str = Field(None, description="안내 지점 유형 (SP: 출발지, EP: 도착지, PP: 경유지, GP: 일반 안내점)", example="SP")


class PedestrianRouteResponseFeatureGeometry(BaseModel):
    """
    보행자 경로 안내 응답의 Feature Geometry 정보를 담는 DTO입니다.
    """

    type: str = Field(..., description="Geometry 유형 (Point, LineString)", example="LineString")
    coordinates: list = Field(..., description="좌표 정보 ([[x1, y1], [x2, y2]], Point에서는 [x, y])", example=[[127.032061691553, 37.2781204926811], [127.032095359532, 37.2781189700618]])


class PedestrianRouteResponseFeature(BaseModel):
    """
    보행자 경로 안내 응답의 Feature 정보를 담는 DTO입니다.
    """

    type: str = Field(..., description="Feature 유형", example="Feature")
    geometry: PedestrianRouteResponseFeatureGeometry = Field(...)
    properties: PedestrianRouteResponseFeatureProperties = Field(...)


class PedestrianRouteResponse(BaseModel):
    """
    보행자 경로 안내 응답 정보를 담는 DTO입니다.
    """

    type: str = Field(..., description="GeoJSON 유형", example="FeatureCollection")
    features: list[PedestrianRouteResponseFeature] = Field(...)
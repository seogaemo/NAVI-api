from typing import Optional
from pydantic import BaseModel, Field


class SearchParams(BaseModel):
    version: int = Field(1, description="API 서비스의 지원 오퍼레이션 버전")
    searchKeyword: str = Field(..., description="시설물명, 상호, 시설 유형, 주소, 전화번호를 검색어로 지정")
    searchType: Optional[str] = Field("all", description="장소 통합 검색 API는 통합(all), 명칭(name), 전화번호(telno)로 총 3가지 검색 유형을 지원")
    areaLLCode: Optional[str] = Field(None, description="지역 대분류 코드 지정")
    areaLMCode: Optional[str] = Field(None, description="지역 중분류 코드를 지정")
    reqCoordType: Optional[str] = Field("WGS84GEO", description="요청 좌표계를 지정")
    resCoordType: Optional[str] = Field("WGS84GEO", description="응답 좌표계를 지정")
    searchtypCd: Optional[str] = Field("A", description="검색 결과 정렬 순서를 정확도순 또는 거리순으로 지정")
    centerLon: Optional[float] = Field(None, description="반경 검색에서 사용하는 중심 경도를 지정")
    centerLat: Optional[float] = Field(None, description="반경 검색에서 사용하는 중심 위도를 지정")
    radius: Optional[int] = Field(None, description="검색 반경(radius)을 지정")
    page: int = Field(1, description="검색 결과 페이지 번호를 지정")
    count: int = Field(20, description="페이지당 검색 결과 수를 지정")
    multiPoint: Optional[str] = Field("N", description="검색할 관심 장소(POI)가 정문, 후문 등 입구가 여러 개인 건물인 경우 기본 건물에 대한 결괏값만 반환할지, 모든 결괏값을 반환할지 지정")
    poiGroupYn: Optional[str] = Field("N", description="검색할 관심 장소(POI)의 부속 시설물에 대한 정보가 있는 경우 그 결괏값을 반환할지 지정")

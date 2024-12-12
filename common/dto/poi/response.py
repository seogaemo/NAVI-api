from typing import List, Optional
from pydantic import BaseModel, Field


class EvCharger(BaseModel):
    operatorId: Optional[str] = Field(None, description="EV 충전소 제공업체")
    stationId: Optional[str] = Field(None, description="충전소 ID")
    chargerId: Optional[str] = Field(None, description="충전기 ID")
    status: Optional[str] = Field(None, description="충전기 상태 정보")
    type: Optional[str] = Field(None, description="충전기 타입 정보")
    powerType: Optional[str] = Field(None, description="EV 충전기 충전량")
    operatorName: Optional[str] = Field(None, description="제공업체명")
    chargingDateTime: Optional[str] = Field(None, description="마지막 충전 시각")
    updateDateTime: Optional[str] = Field(None, description="충전 관련 데이터 최종 변경 시각")
    isFast: Optional[str] = Field(None, description="급속 충전 여부")
    isAvailable: Optional[str] = Field(None, description="충전기 사용 가능 여부")


class NewAddress(BaseModel):
    centerLat: Optional[float] = Field(None, description="중심점 위도 좌표")
    centerLon: Optional[float] = Field(None, description="중심점 경도 좌표")
    frontLat: Optional[float] = Field(None, description="장소(시설물) 입구 위도 좌표")
    frontLon: Optional[float] = Field(None, description="장소(시설물) 입구 경도 좌표")
    roadName: Optional[str] = Field(None, description="도로명")
    bldNo1: Optional[str] = Field(None, description="건물번호의 본번")
    bldNo2: Optional[str] = Field(None, description="건물번호의 부번")
    roadId: Optional[str] = Field(None, description="도로명 코드")
    fullAddressRoad: Optional[str] = Field(None, description="전체 도로명 주소")


class GroupSub(BaseModel):
    subPkey: Optional[str] = Field(None, description="관심 장소(POI) 식별자")
    subSeq: Optional[str] = Field(None, description="부속 시설물의 일련번호")
    subName: Optional[str] = Field(None, description="부속 시설물의 명칭")
    subCenterY: Optional[float] = Field(None, description="부속 시설물의 중심 Y 좌표")
    subCenterX: Optional[float] = Field(None, description="부속 시설물의 중심 X 좌표")
    subNavY: Optional[float] = Field(None, description="부속 시설물의 입구 Y 좌표")
    subNavX: Optional[float] = Field(None, description="부속 시설물의 입구 X 좌표")
    subRpFlag: Optional[str] = Field(None, description="부속 시설물의 길안내 요청에 필요한 값")
    subPoiId: Optional[str] = Field(None, description="부속 시설물의 관심 장소(POI) ID")
    subNavSeq: Optional[str] = Field(None, description="부속 시설물의 입구 번호")
    subParkYn: Optional[str] = Field(None, description="부속 시설물의 주차 여부")
    subClassCd: Optional[str] = Field(None, description="부속 시설물의 업종 코드")
    subClassNmA: Optional[str] = Field(None, description="부속 시설물의 업종 대분류명")
    subClassNmB: Optional[str] = Field(None, description="부속 시설물의 업종 중분류명")
    subClassNmC: Optional[str] = Field(None, description="부속 시설물의 업종 소분류명")
    subClassNmD: Optional[str] = Field(None, description="부속 시설물의 업종 세분류명")


class Poi(BaseModel):
    id: Optional[str] = Field(None, description="관심 장소(POI) ID")
    pkey: Optional[str] = Field(None, description="관심 장소(POI) 식별자")
    navSeq: Optional[str] = Field(None, description="장소(시설물)의 입구 일련번호")
    collectionType: Optional[str] = Field(None, description="문서의 컬렉션(address, poi) 출처")
    name: Optional[str] = Field(None, description="장소명(시설물 등) 및 업체명")
    telNo: Optional[str] = Field(None, description="전화번호")
    frontLat: Optional[float] = Field(None, description="장소(시설물) 입구 위도 좌표")
    frontLon: Optional[float] = Field(None, description="장소(시설물) 입구 경도 좌표")
    noorLat: Optional[float] = Field(None, description="중심점 위도 좌표")
    noorLon: Optional[float] = Field(None, description="중심점 경도 좌표")
    upperAddrName: Optional[str] = Field(None, description="표출 주소 대분류명(시/도)")
    middleAddrName: Optional[str] = Field(None, description="표출 주소 중분류명(시/군/구)")
    lowerAddrName: Optional[str] = Field(None, description="표출 주소 소분류명(읍/면/동)")
    detailAddrName: Optional[str] = Field(None, description="표출 주소 세분류명(동/호/층)")
    mlClass: Optional[str] = Field(None, description="산/대지 구분(구주소)")
    firstNo: Optional[str] = Field(None, description="주소 본번")
    secondNo: Optional[str] = Field(None, description="주소 부번")
    roadName: Optional[str] = Field(None, description="도로명")
    firstBuildNo: Optional[str] = Field(None, description="건물번호의 본번(새주소)")
    secondBuildNo: Optional[str] = Field(None, description="건물번호의 부번(새주소)")
    radius: Optional[str] = Field(None, description="요청 좌표에서 떨어진 거리")
    bizName: Optional[str] = Field(None, description="대표 업종명")
    upperBizName: Optional[str] = Field(None, description="업종 대분류명")
    middleBizName: Optional[str] = Field(None, description="업종 중분류명")
    lowerBizName: Optional[str] = Field(None, description="업종 소분류명")
    detailBizName: Optional[str] = Field(None, description="업종 상세 분류명")
    rpFlag: Optional[str] = Field(None, description="길안내 요청에 필요한 값")
    parkFlag: Optional[int] = Field(None, description="주차 가능 유무")
    detailInfoFlag: Optional[int] = Field(None, description="관심 장소(POI) 상세 정보 유무")
    desc: Optional[str] = Field(None, description="검색된 관심 장소(POI)에 대한 소개")
    dataKind: Optional[str] = Field(None, description="데이터 구분자")
    zipCode: Optional[str] = Field(None, description="우편번호")
    groupSubLists: Optional[List[GroupSub]] = Field(None, description="검색한 관심 장소(POI)의 그룹 하위 목록")
    newAddressList: Optional[List[NewAddress]] = Field(None, description="새주소 목록")
    evChargers: Optional[List[EvCharger]] = Field(None, description="충전기 목록")


class Pois(BaseModel):
    poi: List[Poi] = Field(..., description="검색 결과의 관심 장소(POI) 정보")


class SearchPoiInfo(BaseModel):
    totalCount: Optional[int] = Field(None, description="조회 결과의 총 개수")
    count: Optional[int] = Field(None, description="페이지당 조회 결과 수")
    page: Optional[int] = Field(None, description="조회한 페이지 번호")
    pois: Optional[Pois] = Field(None, description="관심 장소(POI) 목록")


class PoiResponse(BaseModel):
    searchPoiInfo: Optional[SearchPoiInfo] = Field(None, description="관심 장소(POI)를 검색한 결과의 정보")
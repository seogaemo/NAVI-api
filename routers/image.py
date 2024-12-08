from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from api.services.image.image_service import Image

router = APIRouter(prefix="/image", tags=["Image"])
image = Image()


@router.get(
    "/original",
    response_class=StreamingResponse,
    description="JPEG Image",
)
async def get_original_images(pointId: str) -> StreamingResponse:
    """
    원본 이미지를 반환하는 함수입니다.
    """

    return image.getImage(pointId)


@router.get(
    "/predicted",
    response_class=StreamingResponse,
    description="JPEG Image",
)
async def get_predicted_images(pointId: str):
    """
    예측된 이미지를 반환하는 함수입니다.
    """

    return image.getPredictedImage(pointId)

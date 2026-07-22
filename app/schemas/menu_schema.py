from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class MenuCreate(BaseModel):
    """메뉴 등록 요청 본문입니다."""

    restaurant_id: int = Field(gt=0, examples=[1], description="음식점 번호")
    name: str = Field(min_length=1, max_length=100, examples=["불고기 버거"])
    description: str | None = Field(default=None, max_length=500, examples=["직화 불고기 패티와 신선한 채소"])
    price: int = Field(ge=0, examples=[7500], description="원 단위 가격")


class MenuUpdate(BaseModel):
    """메뉴 수정 요청 본문입니다. 보내지 않은 필드는 기존 값을 유지합니다."""

    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    price: int | None = Field(default=None, ge=0)


class MenuPublic(BaseModel):
    """DB에서 조회하여 클라이언트로 반환할 메뉴 데이터입니다."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    restaurant_id: int
    name: str
    description: str | None
    price: int
    created_at: datetime

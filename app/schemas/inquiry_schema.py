from datetime import datetime

from pydantic import BaseModel, Field


class InquiryCreate(BaseModel):
    member_id: str = Field(min_length=1, examples=["member-001"])
    restaurant_id: str = Field(min_length=1, examples=["restaurant-001"])
    inquiry_content: str = Field(
        min_length=1,
        max_length=1000,
        examples=["주문한 음식이 아직 도착하지 않았습니다."],
    )


class InquiryUpdate(BaseModel):
    inquiry_content: str = Field(
        min_length=1,
        max_length=1000,
        examples=["주문한 음식이 아직 도착하지 않았습니다."],
    )
    status: str = Field(
        pattern="^(답변대기|답변완료)$",
        examples=["답변완료"],
    )
    answer: str | None = Field(
        default=None,
        max_length=1000,
        examples=["불편을 드려 죄송합니다. 확인 후 도움드리겠습니다."],
    )


class InquiryPublic(BaseModel):
    id: str = Field(examples=["20260722100000000001"])
    member_id: str
    restaurant_id: str
    inquiry_content: str
    status: str
    answer: str | None
    created_at: datetime
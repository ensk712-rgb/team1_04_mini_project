from datetime import datetime

from pydantic import BaseModel, Field


class MemberCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50, examples=["홍길동"])
    callnumber: str = Field(min_length=1, max_length=20, examples=["010-1234-5678"])


class MemberUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=50, examples=["김철수"])
    callnumber: str = Field(min_length=1, max_length=20, examples=["010-9876-5432"])


class MemberPublic(BaseModel):
    id: str = Field(examples=["20260721170435315246"])
    name: str
    callnumber: str
    created_at: datetime

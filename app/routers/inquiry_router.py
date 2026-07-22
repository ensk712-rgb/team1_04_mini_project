from fastapi import APIRouter, HTTPException

from app.core.api_response import ApiResponse
from app.schemas.inquiry_schema import InquiryCreate, InquiryUpdate
from app.services.inquiry_service import (
    inquiry_create,
    inquiry_delete,
    inquiry_get,
    inquiry_get_all,
    inquiry_update,
)


inquiry_router = APIRouter(
    prefix="/inquiries",
    tags=["Delivery Inquiries"],
)


# 1. 문의 등록
@inquiry_router.post("", status_code=201)
def create(inquiry: InquiryCreate) -> ApiResponse:
    created_inquiry = inquiry_create(inquiry)

    if created_inquiry is None:
        raise HTTPException(
            status_code=500,
            detail="문의 등록에 실패했습니다.",
        )

    return ApiResponse(
        success=True,
        message="문의가 등록되었습니다.",
        data=created_inquiry,
    )


# 2. 문의 전체 조회
@inquiry_router.get("")
def get_all() -> ApiResponse:
    inquiries = inquiry_get_all()

    return ApiResponse(
        success=True,
        message="문의 목록 조회에 성공했습니다.",
        data=inquiries,
    )


# 3. 문의 상세 조회
@inquiry_router.get("/{inquiry_id}")
def get(inquiry_id: str) -> ApiResponse:
    inquiry = inquiry_get(inquiry_id)

    if inquiry is None:
        raise HTTPException(
            status_code=404,
            detail=f"문의 ID {inquiry_id}를 찾을 수 없습니다.",
        )

    return ApiResponse(
        success=True,
        message="문의 조회에 성공했습니다.",
        data=inquiry,
    )


# 4. 문의 수정 및 관리자 답변
@inquiry_router.put("/{inquiry_id}")
def update(inquiry_id: str, inquiry: InquiryUpdate) -> ApiResponse:
    updated_inquiry = inquiry_update(inquiry_id, inquiry)

    if updated_inquiry is None:
        raise HTTPException(
            status_code=404,
            detail=f"문의 ID {inquiry_id}를 찾을 수 없습니다.",
        )

    return ApiResponse(
        success=True,
        message="문의가 수정되었습니다.",
        data=updated_inquiry,
    )


# 5. 문의 삭제
@inquiry_router.delete("/{inquiry_id}")
def delete(inquiry_id: str) -> ApiResponse:
    deleted_inquiry = inquiry_delete(inquiry_id)

    if deleted_inquiry is None:
        raise HTTPException(
            status_code=404,
            detail=f"문의 ID {inquiry_id}를 찾을 수 없습니다.",
        )

    return ApiResponse(
        success=True,
        message="문의가 삭제되었습니다.",
        data=deleted_inquiry,
    )
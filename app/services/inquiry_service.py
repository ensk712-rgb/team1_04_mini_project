from datetime import datetime
from zoneinfo import ZoneInfo

from app.core.supabase_client import get_supabase
from app.schemas.inquiry_schema import (
    InquiryCreate,
    InquiryPublic,
    InquiryUpdate,
)


# 1. 문의 등록
def inquiry_create(inquiry: InquiryCreate) -> InquiryPublic | None:
    supabase = get_supabase()
    now = datetime.now(ZoneInfo("Asia/Seoul"))

    result = (
        supabase.table("delivery_inquiries")
        .insert(
            {
                "id": now.strftime("%Y%m%d%H%M%S%f"),
                "member_id": inquiry.member_id,
                "restaurant_id": inquiry.restaurant_id,
                "inquiry_content": inquiry.inquiry_content,
                "status": "답변대기",
                "answer": None,
                "created_at": now.isoformat(),
            }
        )
        .execute()
    )

    if not result.data:
        return None

    return InquiryPublic.model_validate(result.data[0])


# 2. 문의 전체 조회
def inquiry_get_all() -> list[InquiryPublic]:
    supabase = get_supabase()

    result = (
        supabase.table("delivery_inquiries")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    return [InquiryPublic.model_validate(item) for item in result.data]


# 3. 문의 상세 조회
def inquiry_get(inquiry_id: str) -> InquiryPublic | None:
    supabase = get_supabase()

    result = (
        supabase.table("delivery_inquiries")
        .select("*")
        .eq("id", inquiry_id)
        .execute()
    )

    if not result.data:
        return None

    return InquiryPublic.model_validate(result.data[0])


# 4. 문의 삭제
def inquiry_delete(inquiry_id: str) -> InquiryPublic | None:
    supabase = get_supabase()

    result = (
        supabase.table("delivery_inquiries")
        .delete()
        .eq("id", inquiry_id)
        .execute()
    )

    if not result.data:
        return None

    return InquiryPublic.model_validate(result.data[0])


# 5. 문의 수정 및 관리자 답변
def inquiry_update(
    inquiry_id: str,
    inquiry: InquiryUpdate,
) -> InquiryPublic | None:
    supabase = get_supabase()

    result = (
        supabase.table("delivery_inquiries")
        .update(
            {
                "inquiry_content": inquiry.inquiry_content,
                "status": inquiry.status,
                "answer": inquiry.answer,
            }
        )
        .eq("id", inquiry_id)
        .execute()
    )

    if not result.data:
        return None

    return InquiryPublic.model_validate(result.data[0])
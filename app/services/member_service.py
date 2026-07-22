# member_service.py
from app.schemas.member_schema import MemberCreate, MemberPublic, MemberUpdate
from app.core.supabase_client import get_supabase
from zoneinfo import ZoneInfo
from datetime import datetime

# 1. 입력
def member_create(member: MemberCreate) -> MemberPublic | None:
    supabase = get_supabase()
    now = datetime.now(ZoneInfo("Asia/Seoul"))

    result = (
        supabase.table("members")
         .insert(
            {
                "id": now.strftime("%Y%m%d%H%M%S%f"),
                "name": member.name,
                "callnumber": member.callnumber,
                "created_at": now.isoformat(),   # timestamptz
            }
        )
        .execute()
    )
    if not result.data:
        return None
    return MemberPublic.model_validate(result.data[0])

# 2. 전체조회
def member_get_all() -> list[MemberPublic]:
    supabase = get_supabase()
    result = (
        supabase.table("members")
        .select("*")
        .execute()
    )
    return [MemberPublic.model_validate(item) for item in result.data]

# 3. 한개조회
def member_get(member_id: str) -> MemberPublic | None:
    supabase = get_supabase()

    result = (
        supabase.table("members")
        .select("*")
        .eq("id", member_id)
        .execute()
    )
    if not result.data:
        return None
    return MemberPublic.model_validate(result.data[0])


# 4. 삭제
def member_delete(member_id: str) -> MemberPublic | None:
    supabase = get_supabase()
    result = (
        supabase.table("members")
        .delete()
        .eq("id", member_id)
        .execute()
    )
    if not result.data:
        return None
    return MemberPublic.model_validate(result.data[0])


# 5. 수정
def member_update(
    member_id: str,
    member: MemberUpdate,
) -> MemberPublic | None:
    supabase = get_supabase()

    result = (
        supabase.table("members")
        .update(
                {
                    "name": member.name,
                    "callnumber": member.callnumber,
                }
            )
            .eq("id", member_id)
            .execute()
    )
    if not result.data:
        return None
    return MemberPublic.model_validate(result.data[0])



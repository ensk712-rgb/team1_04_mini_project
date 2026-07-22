# member_router.py

from fastapi import APIRouter, HTTPException

from app.schemas.member_schema import MemberCreate, MemberUpdate
from app.services.member_service import (
    member_create,
    member_delete,
    member_get,
    member_get_all,
    member_update,
)
from app.core.api_response import ApiResponse

member_router = APIRouter(tags=["Member"])

# 200: 정상 - 정상 실행 되면 자동 전송
# 400: 잘못된 요청
# 401: 로그인 필요
# 403: 권한 없음
# 404: 데이터 없음
# 409: 중복 데이터
# 422: 입력값 검증 실패
# 500: 서버 또는 DB 처리 실패

# 1. create
@member_router.post("/member/create")
def create(member: MemberCreate) -> ApiResponse:
    created_member = member_create(member)
    if created_member is None:
        raise HTTPException(
            status_code=500,
            detail="회원 등록에 실패했습니다.",
        )
    response = ApiResponse(
        success = True,
        message="회원이 등록되었습니다.",
        data = created_member
    )
    return response

# 2. 한개 조회
@member_router.get("/member/get/{member_id}")
def get(member_id: str) -> ApiResponse:

    member = member_get(member_id)
    if member is None:
        raise HTTPException(
            status_code=404,
            detail=f"회원 ID {member_id}를 찾을 수 없습니다."
        )
    response = ApiResponse(
        success = True,
        message="회원 조회에 성공했습니다.",
        data = member
    )
    return response

# 3. 전체 조회
@member_router.get("/member/getall")
def get_all() -> ApiResponse:
    members = member_get_all()
    response = ApiResponse(
        success = True,
        message="회원 목록 조회에 성공했습니다.",
        data = members
    )
    return response

# 4. 한개 삭제
@member_router.delete("/member/delete/{member_id}")
def delete(member_id: str) -> ApiResponse:
    member = member_delete(member_id)
    if member is None:
        raise HTTPException(
            status_code=404,
            detail=f"회원 ID {member_id}를 찾을 수 없습니다."
        )
    response = ApiResponse(
        success = True,
        message="회원이 삭제되었습니다.",
        data = member
    )
    return response

# 5. 수정
@member_router.put("/member/{member_id}")
def update(member_id: str, member: MemberUpdate) -> ApiResponse:
    updated_member = member_update(member_id, member)
    if updated_member is None:
        raise HTTPException(
            status_code=404,
            detail=f"회원 ID {member_id}를 찾을 수 없습니다."
        )
    response = ApiResponse(
        success = True,
        message="회원이 수정되었습니다.",
        data = updated_member
    )
    return response

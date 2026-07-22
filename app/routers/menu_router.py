from fastapi import APIRouter, HTTPException, Query, status

from app.core.api_response import ApiResponse
from app.schemas.menu_schema import MenuCreate, MenuUpdate
from app.services.menu_service import create_menu, delete_menu, get_menu, get_menus, update_menu

menu_router = APIRouter(prefix="/menus", tags=["메뉴 관리"])


@menu_router.get("", response_model=ApiResponse)
def read_menus(
    restaurant_id: int | None = Query(default=None, gt=0, description="음식점 번호로 필터링"),
) -> ApiResponse:
    menus = get_menus(restaurant_id)
    message = "음식점 메뉴 목록 조회에 성공했습니다." if restaurant_id else "전체 메뉴 목록 조회에 성공했습니다."
    return ApiResponse(success=True, message=message, data=menus)


@menu_router.get("/{menu_id}", response_model=ApiResponse)
def read_menu(menu_id: int) -> ApiResponse:
    menu = _get_or_404(menu_id)
    return ApiResponse(success=True, message="메뉴 상세 조회에 성공했습니다.", data=menu)


@menu_router.post("", response_model=ApiResponse, status_code=status.HTTP_201_CREATED)
def add_menu(menu: MenuCreate) -> ApiResponse:
    created_menu = create_menu(menu)
    if created_menu is None:
        raise HTTPException(status_code=500, detail="메뉴 등록에 실패했습니다.")
    return ApiResponse(success=True, message="메뉴가 등록되었습니다.", data=created_menu)


@menu_router.put("/{menu_id}", response_model=ApiResponse)
def edit_menu(menu_id: int, menu: MenuUpdate) -> ApiResponse:
    updated_menu = update_menu(menu_id, menu)
    if updated_menu is None:
        raise HTTPException(status_code=404, detail=f"메뉴 ID {menu_id}를 찾을 수 없습니다.")
    return ApiResponse(success=True, message="메뉴가 수정되었습니다.", data=updated_menu)


@menu_router.delete("/{menu_id}", response_model=ApiResponse)
def remove_menu(menu_id: int) -> ApiResponse:
    deleted_menu = delete_menu(menu_id)
    if deleted_menu is None:
        raise HTTPException(status_code=404, detail=f"메뉴 ID {menu_id}를 찾을 수 없습니다.")
    return ApiResponse(success=True, message="메뉴가 삭제되었습니다.", data=deleted_menu)


def _get_or_404(menu_id: int):
    menu = get_menu(menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail=f"메뉴 ID {menu_id}를 찾을 수 없습니다.")
    return menu

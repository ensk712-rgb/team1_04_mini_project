"""menu_items 테이블에 접근하는 데이터 처리 계층입니다."""

from app.core.supabase_client import get_supabase
from app.schemas.menu_schema import MenuCreate, MenuPublic, MenuUpdate

TABLE_NAME = "menu_items"


def create_menu(menu: MenuCreate) -> MenuPublic | None:
    """메뉴를 저장하고 DB가 생성한 id 및 created_at을 포함해 반환합니다."""
    result = get_supabase().table(TABLE_NAME).insert(menu.model_dump()).execute()
    return _first_or_none(result.data)


def get_menus(restaurant_id: int | None = None) -> list[MenuPublic]:
    """전체 메뉴 또는 지정 음식점 메뉴를 생성일 역순으로 조회합니다."""
    query = get_supabase().table(TABLE_NAME).select("*")
    if restaurant_id is not None:
        query = query.eq("restaurant_id", restaurant_id)
    result = query.order("created_at", desc=True).execute()
    return [MenuPublic.model_validate(item) for item in result.data]


def get_menu(menu_id: int) -> MenuPublic | None:
    result = get_supabase().table(TABLE_NAME).select("*").eq("id", menu_id).execute()
    return _first_or_none(result.data)


def update_menu(menu_id: int, menu: MenuUpdate) -> MenuPublic | None:
    """exclude_unset으로 전달된 필드만 수정하여 부분 수정처럼 안전하게 처리합니다."""
    update_data = menu.model_dump(exclude_unset=True)
    if not update_data:
        return get_menu(menu_id)
    result = get_supabase().table(TABLE_NAME).update(update_data).eq("id", menu_id).execute()
    return _first_or_none(result.data)


def delete_menu(menu_id: int) -> MenuPublic | None:
    result = get_supabase().table(TABLE_NAME).delete().eq("id", menu_id).execute()
    return _first_or_none(result.data)


def _first_or_none(rows: list[dict]) -> MenuPublic | None:
    if not rows:
        return None
    return MenuPublic.model_validate(rows[0])

# 음식 배달 메뉴 API 프로젝트 계획서

## 1. 프로젝트 개요

음식 배달 앱의 핵심 기능 중 하나인 메뉴 관리 기능을 구현한다. 사용자는 음식점별 메뉴를 조회하고, 관리자는 메뉴를 등록·수정·삭제할 수 있다. 메뉴 데이터는 Supabase PostgreSQL에 저장하고 FastAPI로 REST API를 제공한다.

## 2. 목표

- 메뉴 데이터를 Supabase에서 관리한다.
- FastAPI 기반 메뉴 CRUD API를 완성한다.
- 요청 데이터의 유효성을 Pydantic으로 검증한다.
- Swagger(`/docs`)에서 API를 테스트할 수 있게 한다.
- GitHub 브랜치와 Pull Request 방식으로 협업한다.

## 3. 데이터베이스 설계

테이블명: `menu_items`

| 컬럼 | 타입 | 설명 |
|---|---|---|
| `id` | TEXT | 메뉴 고유 ID, 기본 키 |
| `restaurant_id` | INTEGER | 음식점 번호 |
| `name` | TEXT | 메뉴명 |
| `description` | TEXT | 메뉴 설명 |
| `price` | INTEGER | 가격, 0 이상 |
| `created_at` | TIMESTAMP | 등록 일시 |

### 사전 점검

현재 테이블의 `id`는 자동 생성되지 않는다. 따라서 아래 둘 중 하나를 팀에서 결정한다.

1. 메뉴 등록 및 초기 INSERT에 `id` 값을 직접 포함한다. 예: `menu-001`
2. `id`를 자동 생성하는 `BIGINT GENERATED ALWAYS AS IDENTITY`로 변경한다.

초보 팀 프로젝트에는 2번을 권장한다. 기존 초기 INSERT문을 거의 수정하지 않고 사용할 수 있기 때문이다.

## 4. 구현 범위

### 필수 기능

| 기능 | HTTP | 경로 | 설명 |
|---|---|---|---|
| 메뉴 목록 | GET | `/menus` | 전체 메뉴 또는 음식점별 메뉴 조회 |
| 메뉴 상세 | GET | `/menus/{menu_id}` | 메뉴 한 건 조회 |
| 메뉴 등록 | POST | `/menus` | 새 메뉴 등록 |
| 메뉴 수정 | PUT | `/menus/{menu_id}` | 메뉴명, 설명, 가격 수정 |
| 메뉴 삭제 | DELETE | `/menus/{menu_id}` | 메뉴 삭제 |

### 선택 확장 기능

- 음식점 테이블(`restaurants`)을 추가해 `restaurant_id`를 외래 키로 연결
- 메뉴명 키워드 검색 및 가격 범위 필터
- 품절 여부(`is_sold_out`) 관리
- 채팅 API로 “치킨 메뉴 추천해줘” 같은 간단한 메뉴 추천
- 주문 및 주문 상세 테이블 추가

## 5. 개발 일정 예시 (5일)

| 일차 | 작업 | 산출물 |
|---|---|---|
| 1일차 | 요구사항 확정, DB SQL 점검·실행, GitHub 역할 분담 | 확정 SQL, 이슈 목록 |
| 2일차 | Supabase 연결, 메뉴 목록·상세 조회 구현 | GET API |
| 3일차 | 메뉴 등록·수정·삭제 구현, 검증 처리 | CRUD API |
| 4일차 | Swagger 테스트, 오류 처리, 채팅 기능 연동 | 테스트 결과 |
| 5일차 | 통합 테스트, README 보완, 발표 자료 준비 | 최종 저장소 |

## 6. 역할 분담 예시

| 역할 | 담당 업무 |
|---|---|
| 팀장/DB 담당 | Supabase 프로젝트, SQL 실행, 환경 변수 및 병합 관리 |
| 백엔드 1 | `menu_router` 작성, 메뉴 조회 API 구현 |
| 백엔드 2 | `menu_service` 및 Supabase CRUD 구현 |
| 테스트·문서 담당 | Swagger 테스트, 예외 사례 정리, README·발표 자료 작성 |

인원이 적다면 한 사람이 여러 역할을 맡되, 각 기능은 서로 다른 브랜치에서 작업한다.

## 7. 구현 순서

1. `food_delivery.sql`의 `menu_items` 테이블을 Supabase에 생성한다.
2. `app/core/supabase_client.py`에서 Supabase 연결을 확인한다.
3. `app/schemas/menu_schema.py`에 메뉴 등록·수정·응답 모델을 작성한다.
4. `app/services/menu_service.py`에 DB 조회와 CRUD 로직을 작성한다.
5. `app/routers/menu_router.py`에 API 경로를 작성한다.
6. `app/main.py`에 메뉴 라우터를 등록한다.
7. `/docs`에서 정상·실패 요청을 모두 테스트한다.

## 8. 완료 기준

- 메뉴 CRUD API가 모두 동작한다.
- 가격 음수, 없는 메뉴 ID 등 잘못된 요청에 적절한 오류 응답을 준다.
- Supabase에서 데이터 변경 결과를 확인할 수 있다.
- README에 설치, 환경 변수, 실행 방법, API 확인 방법이 정리되어 있다.
- GitHub에 `.env`와 비밀 키가 포함되지 않는다.

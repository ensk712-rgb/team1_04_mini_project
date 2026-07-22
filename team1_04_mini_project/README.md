# 음식 배달 메뉴 API

FastAPI와 Supabase를 사용해 음식점별 메뉴를 조회·등록·수정·삭제하는 미니 프로젝트입니다.

## 기능

- 음식점 번호별 메뉴 조회
- 메뉴 상세 조회
- 메뉴 등록, 수정, 삭제
- 가격이 0원 이상인지 검증
- 채팅 API를 통한 메뉴 추천 기능 확장

## 기술 스택

- Python
- FastAPI
- Pydantic
- Supabase (PostgreSQL)
- Uvicorn

## 프로젝트 구조

```text
app/
├── core/       # Supabase 연결, 공통 응답, 환경 설정
├── routers/    # API 엔드포인트
├── schemas/    # 요청·응답 데이터 모델
├── services/   # 메뉴 및 채팅 비즈니스 로직
├── sql/        # Supabase에서 실행할 SQL
└── main.py     # FastAPI 앱 실행 진입점
```

## 실행 방법

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

서버 실행 후 API 문서는 아래 주소에서 확인합니다.

```text
http://127.0.0.1:8000/docs
```

## 데이터베이스 설정

1. Supabase에서 새 프로젝트를 만듭니다.
2. SQL Editor에서 `app/sql/food_delivery.sql`의 테이블 생성문을 실행합니다.
3. `.env`에 Supabase 접속 정보를 설정합니다. 실제 키는 GitHub에 올리지 않습니다.

```env
SUPABASE_URL=프로젝트_URL
SUPABASE_KEY=프로젝트_API_KEY
```

## 메뉴 데이터 주의사항

현재 `menu_items.id`가 `TEXT PRIMARY KEY`입니다. 따라서 메뉴를 추가할 때 `id`를 직접 넣어야 합니다.
초기 메뉴 INSERT문에서 `id`를 생략하려면, 테이블의 `id`를 자동 생성 방식으로 변경해야 합니다.

## 협업 규칙

1. `main` 브랜치에는 직접 push하지 않습니다.
2. 작업 전 `git pull origin main`을 실행합니다.
3. 기능별 브랜치에서 작업합니다. 예: `feature/menu-api`
4. 완료 후 Pull Request를 만들고 팀원 1명 이상이 확인한 뒤 병합합니다.
5. `.env`, `.venv`는 GitHub에 올리지 않습니다.

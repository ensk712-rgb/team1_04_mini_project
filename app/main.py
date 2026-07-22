from fastapi import FastAPI
from app.routers.chat_router import chat_router
from app.routers.product_router import product_router
import app.core.chat_config  

tags_metadata = [
    {
        "name": "Chat",
        "description": "Gemini 모델을 사용해 사용자 메시지에 답변합니다.",
    },
    {
        "name": "Product",
        "description": "Supabase에 저장된 상품을 생성·조회·수정·삭제합니다.",
    },
]

app = FastAPI(title="Main App")

app.include_router(chat_router)
app.include_router(product_router)

# 04_mini_project 폴더에서
# uvicorn app.tkhan:app --reload
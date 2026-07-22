from fastapi import FastAPI
# from app.routers.chat_router import chat_router
# from app.routers.product_router import product_router
from app.routers.inquiry_router import *
from app.routers.member_router import *
from app.routers.menu_router import *
import app.core.chat_config  

app = FastAPI(title="Main App")

app.include_router(inquiry_router)
app.include_router(member_router)
app.include_router(menu_router)

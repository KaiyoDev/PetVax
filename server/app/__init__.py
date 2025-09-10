from fastapi import FastAPI
# Import router
from .routes import router as api_router
# Import DB
from .utils import get_db, Base, engine
# Khởi tạo app
app = FastAPI(
    title="PetVax API",
    description="API hệ thống quản lý tiêm chủng thú cưng",
    version="1.0.0"
)
# router
app.include_router(api_router)
# Tạo DB
Base.metadata.create_all(bind=engine)

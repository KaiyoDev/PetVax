from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI(title="PetVax API")

# Đăng ký route
app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Xin Chao PetVax Backend"}


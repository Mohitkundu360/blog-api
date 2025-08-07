from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.models import Base
from app.database import engine

Base.metadata.create_all(bind=engine)


app = FastAPI()


# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog API"}


# Include auth routes
app.include_router(auth_router)

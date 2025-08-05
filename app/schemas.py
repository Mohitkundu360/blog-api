from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class PostCreate(BaseModel):
    title: str
    content: str


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    owner: UserOut

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

# ✅ Move this outside any class
class TokenResponse(BaseModel):
    access_token: str
    token_type: str

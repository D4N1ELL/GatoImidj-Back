from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    id: int
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

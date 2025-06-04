from fastapi import APIRouter, HTTPException
from api.models import User, UserCreate
from typing import List
from api.utils import hash_password

router = APIRouter(prefix="/users", tags=["users"])

# Fake DB
users_db: List[User] = []

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    new_user = User(
        id=user.id,
        username=user.username,
        hashed_password=hash_password(user.password)
    )
    users_db.append(new_user)
    return new_user

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

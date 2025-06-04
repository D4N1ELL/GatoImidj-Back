from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/memes", tags=["memes"])

class Meme(BaseModel):
    id: int
    title: str
    url: str
    uploaded_by: str

# Dummy DB
memes_db = [
    {"id": 1, "title": "Grumpy Cat", "url": "/catmemes/grumpy.png", "uploaded_by": "admin"},
]

@router.get("/", response_model=List[Meme])
async def list_memes():
    return memes_db

@router.post("/", response_model=Meme)
async def upload_meme(meme: Meme):
    memes_db.append(meme.dict())
    return meme

@router.get("/{meme_id}", response_model=Meme)
async def get_meme(meme_id: int):
    for meme in memes_db:
        if meme["id"] == meme_id:
            return meme
    return {"error": "Meme not found"}

@router.delete("/{meme_id}")
async def delete_meme(meme_id: int):
    global memes_db
    memes_db = [m for m in memes_db if m["id"] != meme_id]
    return {"message": "Deleted"}

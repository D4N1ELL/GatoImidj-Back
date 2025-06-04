from fastapi import APIRouter, HTTPException
from models import Meme
from api.routes.users import liked_memes_by_user
from api.routes.memes import memes

router = APIRouter(prefix="/likes", tags=["likes"])

@router.post("/{user_id}/{meme_id}")
def like_meme(user_id: int, meme_id: int):
    liked = liked_memes_by_user.get(user_id)
    if liked is None:
        raise HTTPException(status_code=404, detail="User not found")
    for meme in memes:
        if meme.id == meme_id:
            if meme not in liked:
                liked.append(meme)
            return {"message": "Meme liked"}
    raise HTTPException(status_code=404, detail="Meme not found")

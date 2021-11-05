from fastapi import APIRouter,Depends,HTTPException,UploadFile,File,Body,Form
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import mode
from enum import Enum
import schemas,models
from database import SessionLocal, engine
from passlib.context import CryptContext
import hashing
from database import get_db
import oauth2,cloudinary
from typing import List
from schemas import Caption

router = APIRouter(prefix='/upvote')




@router.post('/{post_id}',tags=['upvote'])
def upvote(post_id: int ,db: Session = Depends(get_db),get_current_user: schemas.TokenData = Depends (oauth2.get_current_user)):
    new_vote = models.UpVote(post_id=post_id, user_id = get_current_user.id)
    try:
        db.add(new_vote)
        db.commit()
        m=db.query(models.Posts).filter(models.Posts.id == post_id).first()
        m.upvote = m.upvote+1
        db.commit()
        db.refresh(new_vote)
        return new_vote
    except:
        return "NO"
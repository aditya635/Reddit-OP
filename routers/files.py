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

router = APIRouter(prefix='/files')

@router.post('/',response_model=schemas.File,tags=['file'])
def upload( sub:int = Form(...) , cap:str = Form(...) , file: UploadFile = File(...) ,db: Session = Depends(get_db), get_current_user: schemas.TokenData = Depends (oauth2.get_current_user)):
    result = cloudinary.uploader.upload(file.file)
    url = result.get("url")
    new_post = models.Posts(caption=cap, url= url , user_id = get_current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    ids = db.query(models.Posts).filter(models.Posts.id == new_post.id).first()
    new_d = models.SubredditPost(sub_id = sub, post_id = ids.id)
    db.add(new_d)
    db.commit()
    db.refresh(new_d)
    return new_post

@router.get('/',response_model= List[schemas.File],tags=['file'])
def getfile(db: Session = Depends(get_db)):
    return db.query(models.Posts).all()

@router.get('/{post_id}',response_model= schemas.File,tags=['file'])
def getfile(post_id:int,db: Session = Depends(get_db)):
    return db.query(models.Posts).filter(models.Posts.id == post_id).first()
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

router = APIRouter(prefix='/comment')




@router.post('/',response_model=schemas.Comment,tags=['comment'])
def setcomment(request:schemas.CommentPost ,db: Session = Depends(get_db),get_current_user: schemas.TokenData = Depends (oauth2.get_current_user)):
    new_comment = models.Comments(parent_id = request.parent_id,comment_text= request.comment_data,post_id=request.post_id, user_id = get_current_user.id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment
'''
@router.post('/',response_model=schemas.Comment,tags=['file'])
def comment(cap:str = Form(...) , file: UploadFile = File(...) ,db: Session = Depends(get_db), get_current_user: schemas.TokenData = Depends (oauth2.get_current_user)):
    result = cloudinary.uploader.upload(file.file)
    url = result.get("url")
    new_image = models.Images(caption=cap, url= url , user_id = get_current_user.id)
    db.add(new_image)
    db.commit()
    db.refresh(new_image)
    return new_image

@router.get('/',response_model= List[schemas.File],tags=['file'])
def getcomment(db: Session = Depends(get_db)):
    return db.query(models.Images).all()
'''
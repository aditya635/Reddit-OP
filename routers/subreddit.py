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

router = APIRouter(prefix='/sub')

@router.post('/',response_model=schemas.Sub,tags=['sub'])
def sub(request:schemas.Sub,db: Session = Depends(get_db), get_current_user: schemas.TokenData = Depends (oauth2.get_current_user)):
    new_sub = models.SubReddit(title=request.title, head = get_current_user.id)
    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)
    return new_sub

@router.get('/',response_model=List[schemas.Sub],tags=['sub'])
def getfile(db: Session = Depends(get_db)):
    return db.query(models.SubReddit).all()

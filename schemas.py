from pydantic import BaseModel
from typing import Optional,List

from database import Base

class Comment(BaseModel):
    comment_text:str
    post_id:int
    user_id:int
    class Config():
        orm_mode=True


class File(BaseModel):
    url: str
    caption :str
    user_id : int
    upvote : int
    comments : Optional[List[Comment]] = []
    class Config():
        orm_mode = True

class Post(BaseModel):
    url: str
    caption :str
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name:str
    email:str
    posts : Optional[List[Post]] = []
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password:str

class CommentPost(BaseModel):
    post_id:int
    comment_data:str

class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Caption(BaseModel):
    caption:str

class Sub(BaseModel):
    title:str
    class Config():
        orm_mode = True

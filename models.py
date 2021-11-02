from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType,URLType
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique= True)
    password = Column(String)
    posts = relationship("Posts",  back_populates="creator")

class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    caption = Column(String)
    url = Column(URLType)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="posts")
    comments = relationship("Comments",back_populates="post")

class Comments(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    comment_text = Column(String)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship("Posts",back_populates="comments")



    
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr
from pydantic.types import conint


class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True


class PostCreate(PostBase):
    pass

# response when user is created
class UserOut(BaseModel):
    email: EmailStr
    id:int
    created_at:datetime

    class Config:
        orm_mode= True

# for response
class Post(PostBase):
    id:int
    created_at:datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode= True


class PostOut(BaseModel):
    Post: Post
    votes: int


class UserCreate(BaseModel):
    email: EmailStr
    password: str




class UserLogin(BaseModel):
    email:EmailStr
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id :Optional[str]= None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
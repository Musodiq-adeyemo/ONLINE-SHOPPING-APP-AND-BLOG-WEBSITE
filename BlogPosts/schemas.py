from pydantic import BaseModel,Field
from typing import List,Optional,Dict
from datetime import datetime
from uuid import UUID, uuid4

class SchemasUser(BaseModel):
    id : int
    email: str
    username : str
    password : str
    lastname : str
    firstname : str
    created_at : datetime 

class UserCreator(BaseModel):
    lastname : str
    firstname : str
    username : str
    email : str
    class Config():
        orm_mode = True

class SchemasBlog(BaseModel):
    id : int
    title: str
    content : str
    author : str
    user_id : int
    posted_at : datetime

class ItemShowStore(BaseModel):
    name :str
    price : float
    barcode : str
    class Config():
        orm_mode = True

class UserBlog(BaseModel):
    id : int
    title : str
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    username : str
    email: str
    lastname : str
    firstname : str
    blogs : List[UserBlog]=[]
    item_user : List[ItemShowStore]= []
    class Config():
        orm_mode = True


class UserLogin(BaseModel):
    username : str
    password:str
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    id : int
    title: str
    content : str
    author : str
    user_id: int
    creator : UserCreator
    class Config():
        orm_mode = True

class UpdateBlog(BaseModel):
    title: str
    content : str
    class Config():
        orm_mode = True

class CreateStore(BaseModel):
    name : str



class ShowStore(BaseModel):
    id : int
    name : str
    items : List[ItemShowStore]= []
    class Config():
        orm_mode = True

class ItemStore(BaseModel):
    id : int
    name : str
    class Config():
        orm_mode = True

class CreateItem(BaseModel):
    name :str
    price : float
    description : str
    barcode : str
    store_id : int
    prod_date : datetime
    user_item : int

class UpdateItem(BaseModel):
    name :str
    price : float
    barcode : str
    store_id : int
    description :str
    user_item : int
    class Config():
        orm_mode = True

class ShowItem(BaseModel):
    id : int
    name :str
    price : float
    barcode : str
    store : ItemStore
    prod_date : datetime
    user : UserCreator
    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token : str
    token_type : str
    class Config():
        orm_mode = True

class TokenData(BaseModel):
    username:Optional[str] = None

class PasswordReset(BaseModel):
    email : str
    username :str

class NewPassword(BaseModel):
    token : str
    password : str

class ItemImg(BaseModel):
    id : int
    name : str
    item_id : int
    class Config():
        orm_mode = True
   

class UserImg(BaseModel):
    id : int
    name : str
    user_id : int
    class Config():
        orm_mode = True

class PostImg(BaseModel):
    id : int
    post_id : int
    name : str
    class Config():
        orm_mode = True
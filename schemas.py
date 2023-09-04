from pydantic import BaseModel
from typing import List
from datetime import date, datetime
from sqlalchemy.sql.sqltypes import Date
#Article inside UserDisplay



class Article(BaseModel):
    title: str
    content: str
    published: bool
    date_created: datetime
    class Config():
        orm_mode=True
    

class UserBase(BaseModel):
     username: str
     email: str
     password: str   


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article]
    class Config():
        orm_mode = True
        
 # user inside ArticleDisplay       
class User(BaseModel):
    id: int
    username: str        
    class Config():
        orm_mode = True
        
class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    date_published: date
    creator_id: int
    
   
class ArticleDisplay(BaseModel):  
    title: str
    content: str
    date_created: datetime
    published: bool
    user: User
    class Config():
        orm_mode = True
 

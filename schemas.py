from pydantic import BaseModel
from typing import List
from datetime import datetime
from typing import Optional

'''
Pydantic models
-> FastAPI uses Pydantic models to validate that the incoming data matches the expected shape and type
-> help in converting complex data types, like ORM objects into JSON-compatible data formats for API responses.
'''

'''   
'orm_mode=True' configuration allows this Pydantic model to read data from an ORM model
'''


#Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool
    # date_created: Optional[datetime] = None
    class Config():
        orm_mode=True
        
        


class UserBase(BaseModel):
     username: str
     email: str
     password: str   


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    class Config():
        orm_mode = True
        
 # user inside ArticleDisplay    
 # simplified version of a user to be used inside the ArticleDisplay model.    
class User(BaseModel):
    id: int
    username: str        
    class Config():
        orm_mode = True
        
class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    # date_created: datetime
    creator_id: int
    
   
class ArticleDisplay(BaseModel):  
    title: str
    content: str
    # date_created: datetime
    published: bool
    user: User
    class Config():
        orm_mode = True
 

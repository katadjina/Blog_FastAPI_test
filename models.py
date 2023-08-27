from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from db import models
from db.database import engine
#Predefined parametr values with Enum

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'
    
    
models.Base.metadata.create_all(engine)    
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

class BlogType(str, Enum):
    short ='short'
    story = 'story'
    howto = 'howto'
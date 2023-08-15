from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
#Predefined parametr values with Enum

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'
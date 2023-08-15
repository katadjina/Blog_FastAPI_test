from fastapi import FastAPI
from fastapi import status
from models import BlogType
from typing import Optional



app = FastAPI()

@app.get('/blog/all')
#setting an optional value for a parameter
def get_all_blogs(page, page_size: Optional[int] = None):
    return {'message' : f'All {page_size} blogs on page {page}'}


@app.get('/blog/type/{type}')
def blog_type(type: BlogType):
    return {'message' : f'Blog type: {type.value}'}



#### Example of error handling
@app.get('/blog/{id}')
def get_blog(id: int):
    if id > 10:
        return {'error' : f'Blog with id {id} not found'}
    else:
      return {'message' : f'Post with id {id}'}



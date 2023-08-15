from fastapi import FastAPI
from models import BlogType



app = FastAPI()

@app.get("/blog/all")
def get_all_blogs():
    return {'message' : 'all posts'}


@app.get("/blog/type/{type}")
def blog_type(type: BlogType):
    return {'message' : f'Blog type: {type.value}'}


@app.get("/blog/{id}")
#received param has to be of type int
def get_blog(id: int):
    return {'message' : f'Post with id {id}'}



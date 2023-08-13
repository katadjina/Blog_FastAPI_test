from fastapi import FastAPI
from models import BlogType



app = FastAPI()

@app.get("/blog/all")
def get_all_blogs():
    return {'message' : 'all posts'}


@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {'message' : f'Blog type: {type}'}


@app.get("/blog/{id}")
#received param has to be of type int
def get_blog(id: int):
    return {'message' : f'Post with id {id}'}



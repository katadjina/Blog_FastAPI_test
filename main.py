from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import user
from router import article
from db import models
from db.database import engine

#FastAPI documentation ->  http://127.0.0.1:8000/docs

#activate VE -> source venv/bin/activate   
#deactive -> deactivate
#Check environment -> which python  (.../bin/python if in venv)
# -> pip install -r requirements.txt
#start server -> uvicorn main:app --reload     

app = FastAPI() ##creates an instance of the FastAPI class, which is your web application.
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)



#testin

@app.get('/test')
def index():
    return {'message': 'testing'}


models.Base.metadata.create_all(engine)
from fastapi import FastAPI, Request
from exception import TestException
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import product
from db import models
from db.database import engine
from fastapi.responses import  JSONResponse
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import HTTPException

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
app.include_router(product.router)


#testin

@app.get('/test')
def index():
    return {'message': 'testing'}





@app.exception_handler(TestException)
def strory_exception_handeler(request: Request, exc: TestException):
    return JSONResponse(
        status_code=418,
        content={'detail' : exc.name}
    )

@app.exception_handler(HTTPException)
def custom_handler(request: Request, exc: TestException):
    return PlainTextResponse(str(exc), status_code=400)

models.Base.metadata.create_all(engine)
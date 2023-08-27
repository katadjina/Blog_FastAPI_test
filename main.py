from fastapi import FastAPI
#import the router file
from router import blog_get
from router import blog_post


#FastAPI documentation ->  http://127.0.0.1:8000/docs

#activate VE -> source venv/bin/activate   
#deactive -> source venv/bin/deactivate
#Check environment -> which python  (.../bin/python if in venv)
# -> pip install -r requirements.txt
#start server -> uvicorn main:app --reload     

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)



#testin

@app.get('/test')
def index():
    return {'message': 'testing'}

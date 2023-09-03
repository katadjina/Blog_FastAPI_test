from fastapi import APIRouter
from fastapi import status, Depends
from fastapi import Response
from models import BlogType
from typing import Optional
from router.blog_post import required_functionality
from enum import Enum



router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


#tags param in the decorator 4 grouping endpoints in the generated API documentation.
@router.get(
    # /blog/ -> removed bc prefix is defined for all the get methods
    '/all',
    # tags=['blog'], -> also predefined in tags
    summary = 'Retrieve all blogs',
    description = 'Lorem Ipsum')
#setting an optional value for a parameter
def get_all_blogs(page = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {'message' : f'All {page_size} blogs on page {page}', 'req' : req_parameter}


@router.get('/type/{type}' ,tags=['blog'])
def blog_type(type: BlogType, req_parameter: dict = Depends(required_functionality)):
    return {'message' : f'Blog type: {type.value}'}



@router.get('/{id}/comments/{comment_id}', tags=['blog', 'comment'],  )
def get_comment(id: int, comment_id: int, valid:bool= True, username: Optional[str] = None, req_parameter: dict = Depends(required_functionality)):
    #adding a desc for the documentation:
    
    """
    Simulates comment retrieval from a blog post. 
    - **id** mandatory
    - **comment_id** mandatory path param
    - **valid** optional query param
    - **username** optional query param
     
    """
    return {'message' : f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}



"""  Example of simple error handling
@app.get('/blog/{id}', status_code=404)
def get_blog(id: int):
    if id > 10:
        #if true -> code=404
        return {'error' : f'Blog with id {id} not found'}
    else:
      return {'message' : f'Post with id {id}'}
"""




@router.get('/{id}' , tags=['blog', 'comment'] ,status_code=status.HTTP_200_OK)

def get_blog(id: int, response: Response, req_parameter: dict = Depends(required_functionality)):
    if id > 10:
        #if true -> code=404
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f'Post with id {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message' : f'Post with id {id}'}




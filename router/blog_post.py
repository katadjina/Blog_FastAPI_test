
from typing import Optional, List, Dict
from fastapi import APIRouter
from fastapi import Query, Path, Body
from pydantic import BaseModel


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

#define the blog model


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    nb_comments: int
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1' : 'val1'}

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data' : blog,
        'version' : version
        }


'''
Demo for extracting data from different parts of a request
(various components of HTTP requests)
(path parameters, query parameters, and the request body) 
using FastAPI's various tools, without DB interaction
'''


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
        blog: BlogModel,
        id: int,
        comment_title: Optional[int] = Query(
            None, 
            title='Id of the comment',
            description='Here goes the description for comment_id',
            alias='commentTitle',
            deprecated=True,
        ),
        content: str = Body(
            ...,
            min_length=3,
            max_length=50,
            regex='^[a-z\s]*$'
        ),
        v: Optional[List[str]] = Query(['1', '2', '3', '4']),
        #comment_id: int = Path(...)):
        comment_id: int = Path(..., gt=2, lte=100)
        ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id,
    }
################################################################
# The function definition includes additional metadata for the function parameters using the Query
# Here's what each parameter in the Query constructor means:



def required_functionality():
    return{'message' : 'just text'}
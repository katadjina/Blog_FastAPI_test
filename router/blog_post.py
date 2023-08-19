from typing import Optional
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

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data' : blog,
        'version' : version
        }



@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, 
            comment_id: int = Query
                (None, 
                    itle='Id of the comment',
                    description='Here goes the description for comment_id',
                    alias= 'commentId',
                    deprecated=True
                ),
                # ellipsis (...) -> Require a value (non-optional parameters)
                # setting a default value: content: str = Body('lorem ipsum')
            content: str = Body(...,
                                min_length=3,
                                max_length=50,
                                regex='^[a-z\s]*$')
            ):
            return {
                'blog': blog,
                'id': id,
                'comment_id': comment_id,
                'content': content
            }
    
################################################################
# The function definition includes additional metadata for the function parameters using the Query
# Here's what each parameter in the Query constructor means:
'''
None: This is the default value for the comment_id parameter. If no value is provided for comment_id, it will default to None.

title: This is a human-readable title for the parameter. It's used for generating documentation and providing a clear description 
of what the parameter represents.

description: This is a longer description that provides more context about the purpose and usage of the parameter.
It's also used for generating documentation to help developers understand how to use the parameter correctly.

alias: This parameter allows you to specify an alternative name (alias) for the parameter. 
In this case, the parameter is named comment_id, but it can also be accessed using the alias commentId.

deprecated: This parameter is set to True, indicating that the comment_id parameter is deprecated.
Deprecation means that the parameter is no longer recommended for use, and developers are encouraged to use an alternative approach or parameter. 
It's a way to signal that the parameter might be removed in the future.
'''
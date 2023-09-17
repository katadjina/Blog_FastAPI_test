from typing import List
from schemas import ArticleBase, ArticleDisplay, UserBase
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from auth.oauth2 import oauth2_scheme, get_current_user

router = APIRouter(
  prefix='/article',
  tags=['article']
)

# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
  return db_article.create_article(db, request)

# Get specific article

#@router.get('/{id}', response_model=ArticleDisplay)
@router.get('/{id}', response_model=ArticleDisplay)
# depending on a token for the authentication
#def get_article(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
# here we dont depend on a token
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  return  db_article.get_article(db, id) 
    
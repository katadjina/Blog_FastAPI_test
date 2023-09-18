from typing import List
from schemas import ArticleBase, ArticleDisplay, UserBase
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from auth.oauth2 import get_current_user, oauth2_scheme

router = APIRouter(
  prefix='/article',
  tags=['article']
)

# Create article
#current_user -> cant add article if not authenticated
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  return db_article.create_article(db, request)

# Get specific article

#@router.get('/{id}', response_model=ArticleDisplay)
@router.get('/{id}')
# depending on a token for the authentication
#def get_article(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
  #return  db_article.get_article(db, id) 
# here we dont depend on a token anymore
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
   return {
     'data' : db_article.get_article(db, id),
     'current_user' : current_user
   }
    
    
@router.get('/', response_model= List[ArticleDisplay])
def get_all_articles(db: Session = Depends(get_db)):
    return db_article.get_all_articles(db)    
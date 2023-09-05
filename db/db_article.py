from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DbArticle
from fastapi import HTTPException, status
from datetime import datetime






def create_article(db: Session, request: ArticleBase):
    new_article =  DbArticle (
        title = request.title,
        content = request.content,
        published = request.published,
        # date_created= datetime.now(),
        user_id = request.creator_id     
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
    
    
    
    
def get_article(db: Session, id: int): 
    article = db.query(DbArticle).filter(DbArticle.id == id).first()   
    if not article:
        # option1 : raise HTTPException(status_code=404, detail="Article not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Article with id {id} not found')
    return article
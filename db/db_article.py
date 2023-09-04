from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DbArticle
from fastapi import HTTPException







def create_article(db: Session, request: ArticleBase):
    new_article =  DbArticle (
        title = request.title,
        content = request.content,
        published = request.published,
        date_published = request.date_published,
        user_id = request.creator.id     
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
    
    
    
    
def get_article(db: Session, id: int): 
    article = db.query(DbArticle).filter(DbArticle.id == id).first()   
    if not article:
            raise HTTPException(status_code=404, detail="Article not found")
    return article
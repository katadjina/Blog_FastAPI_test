from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


#USER - Article -> 2way relationship

class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True )
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DbArticle', back_populates='user')
    
    
class DbArticle(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True )
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    # date_created: Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))  #ponting to the 'users' table / 'id' column
    user = relationship("DbUser", back_populates='items')

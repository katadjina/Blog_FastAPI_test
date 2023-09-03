from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List


router = APIRouter(
    prefix='/user',
    tags=['user']
)


#Create user
@router.post('/', response_model= UserDisplay) #dont show password
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)



#read all
@router.get('/', response_model= List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


#read one
@router.get('/{id}', response_model= UserDisplay)
def get_user(id: int, db:Session = Depends(get_db)):
    return db_user.get_user(db ,id)


#update


#delete
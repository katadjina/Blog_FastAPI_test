from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List
from fastapi import HTTPException


router = APIRouter(
    prefix='/user',
    tags=['user']
)
#Implementing @router routes

#Create user
@router.post('/', response_model= UserDisplay) #dont show password #??
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
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)

#delete

'''
@router.get('/delete/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    return  db_user.delete_user(db, id)
'''    

#with condition: 
@router.get('/delete/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db_user.delete_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User successfully deleted"}
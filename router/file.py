from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi.responses import FileResponse

router = APIRouter(
    prefix='/file',
    tags=['file']
)

#POST endpoint
@router.post('/') #decorator
def get_file(file: bytes = File(...)): #endpoint function
    content =file.decode('utf-8')
    lines = content.split('\n')
    return {'lines' : lines}



@router.post('/uploadfile') #decorator
def get_upload_file(upload_file: UploadFile= File(...)) :
    #define destination where the file will be stored:
    path = f"files/{upload_file.filename}"
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return {
       # 'filename' : upload_file.filename
       'filename' : path,
       'type' : upload_file.content_type
     }
    
    
@router.get('/download/{name}' , response_class=FileResponse) 
def get_file(name: str):
    path = f'files/{name}'
    return path   

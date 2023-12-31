from fastapi import APIRouter, Cookie, Header, Form
from fastapi.responses import Response, HTMLResponse
from starlette.responses import PlainTextResponse
from typing import Optional, List
import time


router = APIRouter(
    prefix= '/product',
    tags = ['product']
    )



products = ['watch' , 'camera', 'phone']



async def time_consuming_functionality():
    time.sleep(5)
    return 'ok'
    

@router.post('/new')
def create_product(name:str = Form(...)):
    products.append(name)
    return products



@router.get('/all')
async def get_all_products():
    await time_consuming_functionality() #adding this function will result in receiving outcome delayed by 5sec
    # return products
    # or custom response, all elements in one string
    data = " ".join(products)
    #return Response(content=data, media_type="text/plain")
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response

@router.get('/withheader')
def get_products(
    response: Response,
    custom_header: Optional[List[str]]= Header(None),
    test_cookie: Optional[str] = Cookie(None)
    ):
    if custom_header:
        response.headers['custom_response_header'] = ", ".join(custom_header)
        return {
            'data': products,
            'custom_header': custom_header,
            'my_cookie': test_cookie
            }
    


@router.get('/{id}' , responses={
    200: {
        "content" : {
            "text/html":{
                "example": "<div> Product </div>"
            }
        },
        "description" : "Returns the HTML for an object"
    },
    404: {
         "content" : {
            "text/plain":{
              "example" : " Product not available"
            }
        },
        "description" : "Cleartext error message"
    }
})
def get_product(id: int):
    if id>len(products):
        out = "Product not available"
        return PlainTextResponse(content=out, media_type="text/plain")
        #pass
    else:
    #returning html
     product = products[id]
     out = f""" 
     <head>
        <style>
        .product {{
            width: 500px;
            height: 30px; 
            border: 2px inset green;  
            background-color: lightblue;   
            text-align: center;   
        }}
        </style>
     </head>   
     <div class="product"> {product} </div>
     """
     return HTMLResponse(content=out, media_type="text/html")
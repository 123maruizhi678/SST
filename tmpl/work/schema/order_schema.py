from pydantic import BaseModel

class Order(BaseModel):
    title:str|None = None
    userid:int|None = None

class OrderResponse(BaseModel):
    code:int = 200
    detail:str = 'ok'
    title:str|None
    userid:int|None

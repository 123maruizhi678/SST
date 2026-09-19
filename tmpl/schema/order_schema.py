from pydantic import BaseModel

class Order(BaseModel):
    title:str|None = None
    userid:int|None = None

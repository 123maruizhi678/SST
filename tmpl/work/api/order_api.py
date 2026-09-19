from fastapi import APIRouter,Depends
from dao.order_dao import *
from schema.order_schema import OrderResponse

orderapi = APIRouter()

@orderapi.get('/orders')
def get_orders(data=Depends(select_orders)):
    l = []
    for i in data:
        l.append({'id':i.id,'title':i.title,'userid':i.userid,'create_date':i.create_date,'update_date':i.update_date})
    return l

@orderapi.post('/orders',response_model=OrderResponse)
def add_order(data=Depends(insert_users)):
    return data


@orderapi.put('/orders',response_model=OrderResponse)
def put_order(data=Depends(update_users)):
    return data

@orderapi.delete('/orders')
def delete_order(data=Depends(delete_users)):
    return data

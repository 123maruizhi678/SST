from fastapi import APIRouter,Depends
from dao.order_dao import *

orderapi = APIRouter()

@orderapi.get('/orders')
def get_orders(data=Depends(select_orders)):
    l = []
    for i in data:
        l.append({'id':i.id,'title':i.title,'userid':i.userid,'create_date':i.create_date,'update_date':i.update_date})
    return l

@orderapi.post('/orders',)
def add_order(data=Depends(insert_users)):
    return {'code':200,'details':'插入成功'}


@orderapi.put('/orders',)
def put_order(data=Depends(update_users)):
    return {'code':200,'details':'更新成功'}

@orderapi.delete('/orders/{id}')
def delete_order(id=Depends(delete_users)):
    return {'code':200,'details':'删除成功'}
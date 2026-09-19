from fastapi import Form,HTTPException
from model.order_model import OrderModel
from schema.order_schema import OrderRequest
from util.database import db

def select_orders():
    try:
        order_list = db.query(OrderModel).all()
        return order_list
    except:
        raise HTTPException(status_code=500,detail="查询异常")

def insert_users(req:OrderRequest=Form()):
    try:
        data = req.model_dump()
        db.add(OrderModel(**data))
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail="查询异常")
    return req.model_dump()

def update_users(id:int,req:OrderRequest=Form()):
    try:
        db.query(OrderModel).filter(OrderModel.id == id) \
            .update(req.model_dump(exclude_unset=True))
    except Exception as e:
        raise HTTPException(status_code=500,detail="更新异常")
    else:
        db.commit()
    return req.model_dump(exclude_unset=True)

def delete_users(id:int):
    try:
        db.query(OrderModel).filter(OrderModel.id == id).delete()
    except Exception as e:
        raise HTTPException(status_code=500,detail="删除异常")
    else:
        db.commit()
    return {'code':200,'details':'删除成功'}

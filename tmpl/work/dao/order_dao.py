from fastapi import Form,HTTPException
from sqlalchemy.orm import sessionmaker
from model.order_model import *
from schema.order_schema import *

Session = sessionmaker(bind=engine,autoflush=False,autocommit=False)
db = Session()

def select_orders():
    try:
        order_list = db.query(Order_Model).all()
        return order_list
    except:
        raise HTTPException(status_code=500,detail="查询异常")

def insert_users(req:Order=Form()):
    try:
        data = req.model_dump()
        db.add(Order_Model(**data))
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail="查询异常")
    return req.model_dump()

def update_users(id:int,req:Order=Form()):
    try:
        db.query(Order_Model).filter(Order_Model.id == id) \
            .update(req.model_dump(exclude_unset=True))
    except Exception as e:
        raise HTTPException(status_code=500,detail="更新异常")
    else:
        db.commit()
    return req.model_dump(exclude_unset=True)

def delete_users(id:int):
    try:
        db.query(Order_Model).filter(Order_Model.id == id) \
            .delete()
    except Exception as e:
        raise HTTPException(status_code=500,detail="删除异常")
    else:
        db.commit()
    return {'code':200,'details':'删除成功'}


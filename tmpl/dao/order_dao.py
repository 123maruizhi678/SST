from fastapi import Form,HTTPException
from sqlalchemy.orm import sessionmaker
from model.order_model import *
from schema.order_schema import *

db_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/ai0824?charset=utf8mb4'
engine = create_engine(db_url,pool_size=50)
Base.metadata.create_all(engine)
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
    except Exception as e:
        print('错误为',e)
    else:
        db.commit()

def update_users(id:int,req:Order=Form()):
    try:
        db.query(Order_Model).filter(Order_Model.id == id) \
            .update(req.model_dump(exclude_unset=True))
    except Exception as e:
        print('错误为',e)
    else:
        db.commit()

def delete_users(id:int):
    try:
        db.query(Order_Model).filter(Order_Model.id == id) \
            .delete()
    except Exception as e:
        print('错误为',e)
    else:
        db.commit()
    finally:
        db.close


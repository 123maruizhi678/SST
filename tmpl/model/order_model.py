from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()
class Order_Model(Base):
    __tablename__ = 'order'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    userid = Column(Integer,nullable=False)
    create_date = Column(DATETIME,default=datetime.now)
    update_date = Column(DATETIME,default=datetime.now,onupdate=datetime.now)

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/ai0824?charset=utf8mb4'
engine = create_engine(db_url,pool_size=50)
Base = declarative_base()

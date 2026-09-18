# 依赖注入
from fastapi import Depends,FastAPI

app = FastAPI()

def funa(a:int,b:int,c:int):
    yield a+b+c

@app.get('/depends',summary='依赖注入')
async def root(d:int,data=Depends(funa)):
     return data+d

# ORM框架
from sqlalchemy import *

# 连接数据库
db_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/ai0824?charset=utf8mb4'
engine = create_engine(db_url # 连接地址
                       ,pool_size=50 # 连接池，放置数据库连接的一个内存池
                       ,echo=True # 执行时打印执行的sql语句
                       )

# 建表
from sqlalchemy.orm import declarative_base,sessionmaker
from datetime import datetime
Base = declarative_base()
class Dept(Base):
    __tablename__ = 'ai0824_dept'
    no = Column(Integer,primary_key=True,autoincrement=True,comment='自增主键')
    name = Column(String(14),nullable=False)
    loc = Column(String(13),nullable=False)
    sex = Column(Enum('男','女'),nullable=False)
    create_date = Column(DATETIME,default=datetime.now,nullable=False)
    update_date = Column(DATETIME,default=datetime.now,onupdate=datetime.now,nullable=False)
# Base.metadata.create_all(engine)
Dept.__table__.create(bind=engine,checkfirst=True)
# Dept.__table__.drop(engine,checkfirst=True)

# 数据操作
Session = sessionmaker(bind=engine
                       ,autoflush=False # 自动将python内存中的数据存到数据库内存中
                       ,autocommit=False # 自动提交
                       )
db = Session()
# 增删改
d1 = Dept(name='zs',loc='adg',sex='男')
db.add(d1)
db.query(Dept).filter(Dept.no>5)\
    .delete()
db.query(Dept).filter(Dept.create_date>=datetime.now(),Dept.sex=='男')\
    .update({'name':'ls','sex':'女'})
db.commit()

db.close()

# 原生sql语句执行
db.execute(text('select * from Dept'))

db = Session()
class dept(Base):
    __tablename__ = 'dept'
    deptno = Column(Integer,primary_key=True)
    dname = Column(String(14))
    loc = Column(String(13))

class emp(Base):
    __tablename__ = 'emp'
    empno = Column(Integer,primary_key=True)
    ename = Column(String(10))
    job = Column(String(14))
    mgr = Column(String(14))
    hiredate = Column(DATETIME)
    sal = Column(Float)
    comm = Column(Float)
    deptno = Column(Integer,ForeignKey('dept.deptno'))

# 单表查询
db.query(dept).first()
db.query(dept).all()
db.query(dept).filter(dept.deptno>20).all()
db.query(dept).where(dept.dname.like('%h%')).all()
db.query(dept).filter(or_(dept.deptno>20,dept.dname=='500')).all()
db.query(dept).order_by(dept.deptno.desc())

# 分组聚合
db.query(dept).limit(2).all()
n=1
m=2
db.query(dept).offset((n-1)*m).limit(m).all()
db.query(emp.deptno,func.count(1).label('num'),func.sum(emp.sal).label('salary'))\
    .group_by(emp.deptno).having(func.count(1)>2).all()

# 多表查询
db.query(dept).join(emp,dept.deptno==emp.deptno).all()
db.query(dept.deptno).outerjoin(emp,dept.deptno==emp.deptno).all()

'''
总结
select            ——>   db.query( 表模型名 )
from  表1
join  表2 on 条件  ——> join(连接的表，条件) / outerjoin(连接的表，条件)
where  筛选条件    ——> filter(条件)
group by 分组字段  ——> group_by(分组的字段)
having 分组后过滤    
02
3.
.——> having(过滤的条件)
order by 排序     ——> order_by( 排序的字段.desc() )
limit 分页        ——> offset(偏移量).limit(数据量)
'''

# 接口连接数据库

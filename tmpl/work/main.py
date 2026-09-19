# 使用orm结合fastapi接口对数据库的订单表进行增删改查
# ① 连接数据库，定义数据库表模型，以及数据库会话工具
# ② 定义请求体模型，编写post接口对数据库的订单表插入数据
# ③ 编写put接口对订单进行更新操作
# ④ 编写get接口对订单进行查询操作
# ⑤ 编写delete接口对订单进行删除操作
# ⑥ 总结下orm跟fastapi接口的结合使用步骤以及简单的语法结构框架

'''
# 思考下：
现在需要创建三个目录，api、model、schema
① api目录里编写一个文件order_api.py ,利用api路由分发，存放编写好的以上四个订单增删改查接口
② model目录里编写一个order_model.py ，存放的是订单表的表模型类
③ schema目录里编写一个 order_schema.py , 存放的是订单表的相关请求体、相应体模型
④ 在项目目录下创建一个 main.py文件，从main.py文件启动整个接口程序
尝试操作下！
'''

from fastapi import FastAPI
from api.order_api import orderapi

app = FastAPI()
app.include_router(orderapi,tags=['订单表'])

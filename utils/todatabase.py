# @Time : 2020/3/24 1:19
# @Author : RongDi

from pymongo import MongoClient


class ToDatabase:
    def __init__(self):
        self.host = "localhost"
        self.port = 27017
        self.dbname = "Spider"
        self.collection = "example"

    def get_mongo(self):
        # 1.连接数据库
        client = MongoClient(self.host, self.port)
        # 2.创建数据库
        db = client[self.dbname]
        # 3.创建collection
        conn = db[self.collection]
        return conn

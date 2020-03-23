# @Time : 2020/3/24 1:19
# @Author : RongDi

from pymongo import MongoClient


class ToDatabase:
    def __init__(self, host="localhost", port=27017, dbname="Spider", collection="example"):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.collection = collection

    def get_mongo(self):
        # 1.连接数据库
        client = MongoClient(self.host, self.port)
        # 2.创建数据库
        db = client[self.dbname]
        # 3.创建collection
        conn = db[self.collection]
        return conn

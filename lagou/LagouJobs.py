# @Time : 2020/3/24 19:08
# @Author : RongDi

import requests
from pyquery.pyquery import PyQuery
import json

"""
通过对搜索框源码分析得到，其是一个get请求，url和参数如下：
    url: https://www.lagou.com/jobs/list_  搜索内容直接拼接在其后，例如：list_java
    参数: 意义未知
        labelWords: 
        fromSearch: true
        suginput: 
事实证明这又是一个假的数据接口，真正的数据接口来自
https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false
采用POST请求，data = {
                "first": "true", # 标记当前页是否为第一页，实际不起作用，注释掉依然可以拿到数据
                "pn": 1, # 第几页
                "kd": "java", # 搜索参数
            }
            爬虫拿到的数据跟页面显示的数据顺序对不上
"""


def get_jobs(search_content, page):
    # 这里应该对search_content先进行url编码
    origin_url = "https://www.lagou.com/jobs/list_" + search_content + "java?labelWords=&fromSearch=true&suginput="
    json_url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Referer": origin_url
    }
    data = {
        "first": True,
        "pn": page,
        "kd": "java",
        #     "sid": "d8cb4650cf824ba78f1200e87821c8ca"
    }
    session = requests.Session()
    session.get(origin_url, headers=headers)
    response = session.post(json_url, data=data, headers=headers)
    print(response.status_code)
    data = json.loads(response.text)
    for name in data["content"]["positionResult"]["result"]:
        print(name["companyFullName"])


def main(search_content):
    for page in range(30):  # 这里并不确定到底有多少页
        get_jobs(search_content, page)
        print(search_content)


if __name__ == '__main__':
    main("python")

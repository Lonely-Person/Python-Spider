# @Time : 2020/3/23 21:11
# @Author : RongDi

import requests
from pyquery.pyquery import PyQuery
import json

"""
门面网址：https://xueqiu.com/hq#
但是数据并不来源于此，通过js请求另一个接口加载的数据
    https://xueqiu.com/service/v5/stock/screener/quote/list
    参数如下：
        page: 1
        size: 60
        order: desc
        orderby: percent
        order_by: percent
        market: CN
        type: sh_sz
        _: 1584973131623  时间戳，但并不检查，只要是一个13位的数字即可
"""


def get_data(url, headers, params):
    html = requests.get(url, headers=headers, params=params, timeout=15)
    if html.status_code == 200:
        data = html.text
        data = json.loads(data)
        data = data["data"]
        count = data["count"]
        stocks = data["list"]
        print(stocks)
        return count


def main():
    headers = {  # 目前请求头只需要加这个即可
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    url = "https://xueqiu.com/service/v5/stock/screener/quote/list"
    params = {
        "page": 1,
        "size": 60,
        "order": "desc",
        "orderby": "percent",
        "order_by": "percent",
        "market": "CN",
        "type": "sh_sz",
        "_": 2000000000000,
    }
    count = get_data(url, headers, params)  # 股票个数，这个数值不变
    if count > 60:
        end_page = count//60 + (count % 60 != 0)  # 有余数则+1
        for page in range(2, end_page+1):
            params["page"] = page
            get_data(url, headers, params)


if __name__ == '__main__':
    main()

import requests

"""
    获取百度首页信息
    version: 0.1
    author: kang99
"""
baidu_info = requests.get("http://www.baidu.com")
inone = baidu_info.status_code
if inone == 200:
    print(baidu_info.text)
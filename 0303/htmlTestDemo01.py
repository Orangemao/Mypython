import requests

resp = requests.get("http://www.baidu.com")
if resp.status_code == 200:
    print(resp.text)

print('_________________')

resp = requests.get("https://www.sohu.com/")
print(resp.status_code)
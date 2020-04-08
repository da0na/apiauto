# coding:utf-8
import requests
url = "http://m.imooc.com/passport/user/login"
data = {
    "username": "12321321",
    "password": "111111",
    "verify": "",
    "referer": "https://m.imooc.com"
}
res = requests.post(url, data).json()
response_url = res['data']['url'][0]
request_url = response_url+"&callback=jQuery21008240514814031887_15086668066"
cookie = requests.get(request_url).cookies
print(cookie)
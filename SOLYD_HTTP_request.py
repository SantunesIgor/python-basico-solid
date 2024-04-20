import requests

headers = {'User-agent': 'Windows 12', 'Referer': 'https://putsreq.com/6vaSIPrna6UeG7WB0clO', 'CF_IPcountry': 'US'}

cookies = {'Last-visit': '10-10-2010'}

data = {'username': 'Igor', 'password': '123123'}

try:
    rqt = requests.post('https://putsreq.com/6vaSIPrna6UeG7WB0clO', headers=headers, cookies=cookies, data=data)
except Exception as e:
    print('erro de requisição: ', e)
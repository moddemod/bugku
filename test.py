import requests

requests = requests.Session()

url = 'https://www.baidu.com'
requests.get(url=url)

import requests
from lxml import etree
import re

test_data = [
    'http://pic2.58cdn.com.cn/zhuanzh/n_v23c3bce18e6a645bcb6a45b53d9585f30.jpg?w=750&h=0',
    '//imgstat.baidu.com/9.gif?rainbow=1&'
]

pat = r'((?:http:|https:)?//(?:[^\s]*)\.(?:png|jpg|jpeg|gif|ico)(?:.*?))'

url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E4%B8%8D%E7%9F%A5%E9%81%93%E5%B9%B2%E5%98%9B'

text = requests.get(url).text
# print(text)
res = re.findall(pat, text)
# print(res)
print(list(map(lambda x: 'https:' + x if x.startswith('//') else x, res)))



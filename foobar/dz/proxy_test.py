import sys
import os
import requests

# print(requests.get('http://httpbin.org/ip', proxies={'https': 'http://163.125.222.109:81182'}).text)


sys.path.append('./t_package')
import t_module

print(sys.path)

print(os.getcwd())

print(os.path.abspath('.'))
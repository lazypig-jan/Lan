
import os
from lan import Config

# 初始化config
cf = Config()

# 提前定义好命令 以后只需要 python/python3 run.py
cmd = 'locust -f ./main.py -P ' + cf.get('web_host')

v = os.popen(cmd).readlines()  # 这个返回值是一个list
print(v)
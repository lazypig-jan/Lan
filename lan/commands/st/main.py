# 统一引用lan里的HttpLocust
#  locust -f ./locust11.py -P 8090
from locust import HttpLocust

from lan import Config
# 引用task.py里的Tasks类 启动和任务单独分开写
from task import Tasks

# 初始化Config
cf = Config()


# 运行 locust -f run.py 默认端口为8089
class Main(HttpLocust):
    # 获取任务
    task_set = Tasks
    # 压测时间
    if cf.get('stop_timeout') != 0:
        stop_timeout = cf.get('stop_timeout')
    # 单位为毫秒
    min_wait = cf.get('min_wait')
    # 单位为毫秒
    max_wait = cf.get('max_wait')
    # 压测域名或者服务器ip
    host = cf.get('domain')

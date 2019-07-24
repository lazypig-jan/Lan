# 统一引用lan里的TaskSet和task
from locust import TaskSet, task
from lan import Log

# 初始化Log logfile=true 生成log文件
log = Log(logfile=True)


# 所有任务
class Tasks(TaskSet):
    # 任务1
    @task(1)
    def task1(self):
        response = self.client.get("/api/getlist/1")
        result = response.json()
        if result['code'] == 200:
            log.info("请求成功")
        else:
            log.error("失败")

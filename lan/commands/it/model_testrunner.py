# coding=utf-8
import time
from unittest2 import suite, TextTestRunner
from lan import FileDb, Log, TestLoader, Yaml, Utils
from model.report import ReporeHtml


# 定义 TestRunner 类
class TestRunner(object):
    def __init__(self, path="../"):
        # 获取项目路径
        self.project_path = path
        # yaml init
        self.yaml_config = Yaml(self.project_path + '/config', 'config')
        # 所有结果
        self.db_all = FileDb(self.project_path + '/temp', 'all')
        # 已完成
        self.db_complete = FileDb(self.project_path + '/temp', 'complete')

        self.all_result = []

    # 先处理一下db文件
    def __db_clean(self):
        Log.debug("1-清除缓存")
        self.db_all.remove()
        # 中断后开始是否继续开始
        if self.yaml_config.get("interruptContinue") is False:
            self.db_complete.remove()

    # 获取未执行的用例
    def __get_case_incomplete(self, method_names):
        all = []
        # 获取db已经完成的用例
        complete = self.db_complete.select()
        # 先获取所以method_name用于后面对比
        all_c_mn = []
        for item in complete:
            all_c_mn.append(item['method_name'])

        # 遍历所有用例
        for mn_item in method_names:
            # method_name 如果不在all_c_mn里面 说明么有测试的
            if mn_item['method_name'] not in all_c_mn:
                all.append(mn_item['case'])

        return all

    @staticmethod
    def __get_discover_cases(discover):
        """
        获取discover里的所以用例 方法名称
        """
        data = []
        for item in discover:
            for i in str(item).split('testMethod='):
                for j in i.split('>'):
                    if 'test_' in j:
                        data.append({
                            'method_name': j,
                            'case': item
                        })
        return data

    @staticmethod
    def __get_result_name(item):
        """
        获取方法名
        """
        return str(item[0]).split(' (')[0]

    # 获取所有 discover
    def __get_runner_discover(self):
        Log.debug("4-获取所有用例")
        # 重写TestLoader 用于后期队列及报错连续执行
        discover = TestLoader().discover(self.project_path + '/apis/', pattern='*_st.py', top_level_dir=None)

        # 获取所有用例和方法名
        method_names = self.__get_discover_cases(discover)

        # 读取config interruptContinue:中断后开始是否继续开始
        if self.yaml_config.get("interruptContinue") is True:
            # 拿到方法名和结果队列比较
            discover = self.__get_case_incomplete(method_names)
        return discover, method_names

    def __runner_run(self, item):
        # 开始run test
        test_suites = suite.TestSuite(item)
        runner = TextTestRunner(verbosity=1)
        result = runner.run(test_suites)
        self.all_result.append(result)

    # 第一步获取 result
    def __get_runner_result(self):
        Log.debug("3-执行runner")
        discover, method_names = self.__get_runner_discover()

        Log.debug("5-执行测试用例")
        for i in discover:
            self.__runner_run(i)

        # 在没有全局值的情况下不需要这两东西
        # self.db_all.inster_all(self.db_all.select())
        # self.db_complete.inster_all(self.db_complete.select())

        Log.debug("6-获取用例结果")
        return {
            'method_names': method_names,
            'result': self.all_result
        }

    # 第二步获取用例返回的各种数据
    def __get_case_return_data(self, method_names, results):
        Log.debug("8-重组数据")
        db = self.db_all.select()
        all_data = []
        # 遍历所有用例方法
        for name in method_names:
            info = {
                'status_type': 'success'
            }
            for result in results:
                # 匹配db里对应的方法
                for item in db:
                    if name['method_name'] in item['method_name']:
                        # 提交
                        info['name'] = item['data']['name']
                        info['url'] = item['data']['url']
                        info['mode'] = item['data']['mode']
                        info['submit_data'] = item['data']['data']
                        # 返回
                        info['code'] = item['result']['status_code']
                        info['status'] = item['result']['status']
                        # 状态类型 正确：success 错误：error 跳过：skipped
                        info['status_type'] = item['result']['status']
                        info['data'] = item['result']['response']
                        info['time'] = item['result']['time']
                        info['msg'] = item['result']['msg']

                # 获取跳过的
                for item in result.skipped:
                    if name['method_name'] in self.__get_result_name(item):
                        info['status_type'] = 'skipped'

                # 获取失败的
                for item in result.failures:
                    if name['method_name'] in self.__get_result_name(item):
                        info['status_type'] = 'error'  # failures

                # 获取错误的
                for item in result.errors:
                    if name['method_name'] in self.__get_result_name(item):
                        info['status_type'] = 'error'

            all_data.append(info)
        return all_data

    # 第三步生成报告
    def __build_report(self, start_time, end_time, case_data):
        Log.debug("8-生成报告")
        ReporeHtml(start_time, end_time, case_data).build()

    # 入口
    def run(self):
        Log.debug("开始执行")

        # 每次进入时清除db
        self.__db_clean()

        # 获取开始时间
        start_time = time.time()
        Log.debug("2-开始时间:" + Utils.get_time(start_time))

        # 执行所有用例
        get_result = self.__get_runner_result()

        # 结束时间
        end_time = time.time()
        Log.debug("7-结束时间" + Utils.get_time(end_time))

        # 获取用例返回的各种数据
        get_case_data = self.__get_case_return_data(get_result['method_names'], get_result['result'])

        # 生成报告
        self.__build_report(start_time, end_time, get_case_data)

        Log.debug("9-总共用时" + str(end_time - start_time) + 's')


if __name__ == '__main__':
    TestRunner().run()

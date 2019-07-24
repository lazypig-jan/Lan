import os
from jinja2 import Template
from lan import Yaml, Utils, Log
from lan.commands.it.apis_tpl_code import get_apis_code_tpl


class Make(object):
    def __init__(self, path='./'):
        # 获取当前执行命令目录
        self.project_path = path
        # yaml init
        self.yaml_apis = Yaml(self.project_path + '/config', 'apis')

    def start(self):
        # 获取config.yaml
        data = self.yaml_apis.get('apis')
        # 进入处理流程
        self.__process(data)

    # 创建__init__.py文件
    @staticmethod
    def __create_init_py(filepath):
        # 获取写入路径
        init_path = filepath + '/__init__.py'
        # init 是个空文件
        Utils.write_file(init_path, '')

    # 开始进入流程
    def __process(self, data):
        # 遍历项目获取模块
        for key in data:
            model_path = self.project_path + '/apis/' + key
            self.__process_project_model_name(model_path, data[key])

    # 创建项目模块目录
    def __process_project_model_name(self, path, data):
        # 创建模块目录
        Utils.mkdir(path)
        # 模块目录下面创建__init__.py
        self.__create_init_py(path)
        for key in data:
            filepath = path + '/' + key + '_st.py'
            if os.path.exists(filepath) is False:
                self.__process_project_test_code(filepath, data[key])

    # 创建测试用例文件+代码
    @staticmethod
    def __process_project_test_code(path, data):
        funs = []
        for key in data['funName']:
            funs.append({
                "name": key,
                "data": data['funName'][key]
            })
        template = Template(get_apis_code_tpl())
        content = template.render(ClassName=data['className'], funs=funs)

        # 写入内容
        Utils.write_file(path, content)


def make(args=None):
    Make(os.getcwd()).start()

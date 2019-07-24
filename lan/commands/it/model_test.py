import os, unittest2, warnings

from lan import FileDb, Log, Yaml


class Test(unittest2.TestCase):
    result = {}
    # 获取项目目录
    project_path = os.path.dirname(os.path.dirname(__file__))
    yaml_config = Yaml(project_path + '/config', 'config')
    yaml_apis = Yaml(project_path + '/config', 'apis')

    # 所有结果
    _db_all = FileDb(project_path + '/temp', 'all')
    # 已完成
    _db_complete = FileDb(project_path + '/temp', 'complete')

    # 获取info
    def _getTestInfo(self):
        # 当前测试用例 class 名称
        class_name = self.__class__.__name__
        # 当前测试用例 方法 名称
        method_name = self._testMethodName
        # 当前测试用例 文件 名称
        file_name = self.__class__.__module__
        file_name = file_name.replace('_st', '')
        # 当前测试用例 路径
        file_path = os.path.basename(os.getcwd())

        # 暂时想到这种解决方法 等以后再来优化这块
        if file_name.find('.') >= 0:
            now_data = 'apis.' + file_name
        else:
            now_data = 'apis.' + file_path + '.' + file_name
        return {
            # 'file_name': file_name,
            'class_name': class_name,  # 类名
            'method_name': method_name,  # 方法名
            'now_data_model': now_data,  # 当前模块路径拼接
            'now_data_fun': now_data + '.funName.' + method_name  # 当前方法的yaml路径拼接
        }

    # 获取data
    def _getData(self):
        # 获取当前用例class名 方法名 等
        get_test_info = self._getTestInfo()
        ''' get_test_info
        'class_name': 'TestUserLogin',
        'method_name': 'test_login',
        'now_data_model': 'apis.user.login',
        'now_data_fun': 'apis.user.login.funName.test_login'
        '''
        # 全局data 用例里可用
        now_data_model = self.yaml_apis.get(get_test_info['now_data_model'])
        data = self.yaml_apis.get(get_test_info['now_data_fun'])

        # 模块公共属性 比如 url mode等
        if 'url' in now_data_model:
            pub_url = now_data_model['url']
        else:
            pub_url = None
        if 'mode' in now_data_model:
            pub_mode = now_data_model['mode']
        else:
            pub_mode = None

        if data != '':
            if 'data' not in data:
                data['data'] = {}
            # 如果test_xx接口没有url或者mode就调用全局的
            if 'url' not in data:
                _url = pub_url  # 给url添加域名
            else:
                _url = data['url']  # 给url添加域名
            data['url'] = self.yaml_config.get('domain') + _url

            if 'mode' not in data:
                data['mode'] = pub_mode

            return data
        else:
            return {}

    # 必须使用@classmethod 装饰器,所有test运行前运行一次
    @classmethod
    def setUpClass(cls):
        # print('run setUpClass\n')
        return

    # 每个测试函数运行前运行
    def setUp(self):
        # 在每个用例里可调用
        self.data = self._getData()

    # 每个测试函数运行完后执行
    def tearDown(self):
        # 忽略掉io告警
        warnings.simplefilter("ignore", ResourceWarning)
        Log.debug(self.result)
        # 保存到db
        if self.result:
            get_test_info = self._getTestInfo()

            self._db_all.inster({
                'method_name': get_test_info['method_name'],
                'data': self.data,
                'result': self.result  # 返回提交的data的json
            })

            if self.yaml_config.get('interruptContinue') is True:
                # Log.debug('-----------------------')
                # demo = self._db_complete.find('method_name',get_test_info['method_name'])
                # Log.debug(demo)
                # 保存到 结果队列
                self._db_complete.inster({
                    'status': 1,
                    'method_name': get_test_info['method_name']
                })

    # 必须使用@classmethod装饰器,所有test运行完后运行一次
    @classmethod
    def tearDownClass(cls):
        # print('测试类运行结束！')
        return

import os
from jinja2 import Template
from lan.utils import Utils
from lan.log import Log


def init_file(path, content=''):
    # 写入内容
    Utils.write_file(path + '/__init__.py', content)


def mkdir(name='NAME'):
    Log.debug('创建目录:' + name)
    # 创建ST目录
    path = name
    Utils.mkdir(path)
    return path


def tpl(tpl_path='', save_path=''):
    Log.debug('创建' + save_path + '文件')
    # 获取路径
    code_path = os.path.dirname(__file__) + tpl_path
    # 基础模板文件
    code = Utils.open_file(code_path)
    # 模板编译
    template = Template(code)
    # 写入内容
    Utils.write_file(save_path, template.render())

import os
from jinja2 import Template
from lan.log import Log
from lan.config import Config
from lan.utils import Utils
from lan.commands.sm.templates_index import get_html
from lan.commands.pub import tpl


def _fun_config(path):
    # 创建ini配置文件
    c = Config(
        path=path
    )
    c.set('log', 'true')
    c.set('port', '8090')


def _fun_write_run(path):
    tpl('/sm/run.py', path + '/run.py')


def _fun_write_index_html(path):
    Log.debug('创建index.html文件')
    # 模板编译
    template = Template(get_html())
    # 写入内容
    Utils.write_file(path + '/index.html', template.render())


def sm():
    # 创建Monitor目录
    path = os.getcwd() + '/Monitor'

    Utils.mkdir(path)
    Log.debug('创建目录:Monitor')
    # 创建配置文件
    _fun_config(path)

    # 创建run.py
    _fun_write_run(path)

    # 创建templates目录
    templates = path + '/templates'
    Utils.mkdir(templates)
    Log.debug('创建目录:templates')

    # 创建index.html
    _fun_write_index_html(templates)


if __name__ == '__main__':
    sm()

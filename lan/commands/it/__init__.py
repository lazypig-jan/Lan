import os
from jinja2 import Template
from lan.log import Log
from lan.utils import Utils

from lan.commands.pub import mkdir, tpl, init_file

from lan.commands.it.config_apis_yaml import get_config_apis_tpl
from lan.commands.it.config_config_yaml import get_config_config_tpl
from lan.commands.it.config_mail_yaml import get_config_mail_tpl
from lan.commands.it.config_repore_yaml import get_config_repore_tpl
from lan.commands.it.config_response_yaml import get_config_response_tpl

from lan.commands.it.model_tpl_chart import get_chart_tpl
from lan.commands.it.model_tpl_content import get_content_tpl
from lan.commands.it.model_tpl_nav import get_nav_tpl
from lan.commands.it.model_tpl_template import get_template_tpl
from lan.commands.it.model_tpl_mail_html import get_maile_html_tpl

from lan.commands.make import Make


# config.yaml
def _fun_config_yaml(path):
    Log.debug("创建 apis.yaml文件")
    Utils.write_file(path + '/apis.yaml', Template(get_config_apis_tpl()).render())

    Log.debug('创建 config.yaml文件')
    Utils.write_file(path + '/config.yaml', Template(get_config_config_tpl()).render())

    Log.debug('创建 mail.yaml文件')
    Utils.write_file(path + '/mail.yaml', Template(get_config_mail_tpl()).render())

    Log.debug('创建 repore.yaml文件')
    Utils.write_file(path + '/repore.yaml', Template(get_config_repore_tpl()).render())

    Log.debug('创建 response.yaml文件')
    Utils.write_file(path + '/response.yaml', Template(get_config_response_tpl()).render())


# model/tpl/chart.html
def _fun_write_model_tpl_chart(path):
    Log.debug('创建model/tpl/chart.html文件')
    # 写入内容
    Utils.write_file(path + '/chart.html', get_chart_tpl())


# model/tpl/content.html
def _fun_write_model_tpl_content(path):
    Log.debug('创建model/tpl/content.html文件')
    # 写入内容
    Utils.write_file(path + '/content.html', get_content_tpl())


# model/tpl/nav.html
def _fun_write_model_tpl_nav(path):
    Log.debug('创建model/tpl/nav.html文件')
    # 写入内容
    Utils.write_file(path + '/nav.html', get_nav_tpl())


# model/tpl/template.html
def _fun_write_model_tpl_template(path):
    Log.debug('创建model/tpl/template.html文件')
    # 写入内容
    Utils.write_file(path + '/template.html', get_template_tpl())


# model/tpl/mail_html.txt
def _fun_write_model_tpl_mail_html(path):
    Log.debug('创建model/tpl/mail_html.txt文件')
    # 写入内容
    Utils.write_file(path + '/mail_html.txt', get_maile_html_tpl())


def it(name="demo"):
    # 创建It目录
    root_path = mkdir(os.getcwd() + '/IT')

    path = mkdir(root_path + '/' + name)

    path_model = path + '/model'

    mkdir(path_model)

    tpl('/it/model_init.py', path_model + '/__init__.py')

    path_model_tpl = path + '/model/tpl'
    mkdir(path_model_tpl)

    path_apis = path + '/apis'
    mkdir(path_apis)

    path_config = path + '/config'
    mkdir(path_config)

    path_apis_user = path_apis + '/user'
    mkdir(path_apis_user)
    init_file(path_apis_user)  # 创建空__init__.py

    mkdir(path + '/temp')

    # 创建yaml文件
    _fun_config_yaml(path_config)

    # 创建入口文件
    tpl('/it/run.py', path + '/run.py')

    # 创建testrunner.py
    tpl('/it/model_testrunner.py', path_model + '/testrunner.py')

    # 创建report.py
    tpl('/it/model_report.py', path_model + '/report.py')

    # 创建test.py
    tpl('/it/model_test.py', path_model + '/test.py')

    # 创建html模板
    _fun_write_model_tpl_chart(path_model_tpl)
    _fun_write_model_tpl_content(path_model_tpl)
    _fun_write_model_tpl_nav(path_model_tpl)
    _fun_write_model_tpl_template(path_model_tpl)
    _fun_write_model_tpl_mail_html(path_model_tpl)

    # 创建login_st.py
    # tpl('/it/apis_login_st.py', path_apis_user + '/login_st.py')
    Make(path).start()


if __name__ == '__main__':
    it()

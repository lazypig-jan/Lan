import os
from jinja2 import Template
# import webbrowser
from lan import Utils, Log, Mail, Yaml


class ReporeHtml(object):
    def __init__(self, start_time, end_time, case_data):
        # 获取项目目录
        self.project_path = os.path.dirname(os.path.dirname(__file__))
        self.start_time = start_time
        self.end_time = end_time
        self.case_data = case_data
        self.report_html_path = self.project_path + '/temp/report.html'
        Utils.remove_file(self.report_html_path)

        # yaml init
        _yaml_path = self.project_path + '/config'
        self.yaml_config = Yaml(_yaml_path, 'config')
        self.yaml_apis = Yaml(_yaml_path, 'apis')
        self.yaml_mail = Yaml(_yaml_path, 'mail')
        self.yaml_repore = Yaml(_yaml_path, 'repore')
        self.yaml_response = Yaml(_yaml_path, 'response')

        # 初始化邮箱
        self._mail = Mail(
            self.yaml_mail.get('host'),
            self.yaml_mail.get('port'),
            self.yaml_mail.get('user'),
            self.yaml_mail.get('passwd')
        )

    # 根据类型获取用例的数量和用例
    def __get_case_info(self, cases=[], stype='all'):
        data = []
        if stype != 'all':
            for item in cases:
                if item['status_type'] == stype:
                    data.append(item)
        else:
            data = cases
        return {
            'len': len(data),
            'cases': data
        }

    # 获取切换菜单html
    def __get_cases_nav_html(self, data):
        cases = self.yaml_repore.get("cases")
        new_data = []
        for k, v in cases.items():
            obj = {'text': v}
            if k == 'all':
                obj['num'] = data['all_case_sum']
                obj['bg'] = '#428bca'
            elif k == 'success':
                obj['num'] = data['success_case_sum']
                obj['bg'] = '#3c763d'
            elif k == 'error':
                obj['num'] = data['errors_case_sum']
                obj['bg'] = '#FF4000'
            else:
                obj['num'] = data['skipped_case_sum']
                obj['bg'] = '#0099CC'
            new_data.append(obj)
        return Template(Utils.open_file(os.path.dirname(__file__) + '/tpl/nav.html')).render(datas=new_data)

    # 获取所有用例内容列表
    def get_cases_content_html(self, data):
        table = self.yaml_repore.get('table')
        new_titles = []
        for k, v in table.items():
            obj = {
                'name': k,
                'text': v
            }
            new_titles.append(obj)

        content = Utils.open_file(os.path.dirname(__file__) + '/tpl/content.html')
        return Template(content).render(datas=data, titles=new_titles)

    # 获取统计图
    def __get_cases_chart_html(self, data):
        return Template(Utils.open_file(os.path.dirname(__file__) + '/tpl/chart.html')).render(data)

    # 获取 输出字段数据 模板可使用的字段
    def get_output_field_data(self):
        title = self.yaml_repore.get("title")

        # 所有
        all_case = self.__get_case_info(self.case_data, 'all')
        # 成功
        success = self.__get_case_info(self.case_data, 'success')
        # 错误
        errors = self.__get_case_info(self.case_data, 'error')
        # 跳过
        skipped = self.__get_case_info(self.case_data, 'skipped')
        data = {
            'title': title,  # str
            'start_time': Utils.get_time(self.start_time),  # str
            'end_time': Utils.get_time(self.end_time),  # str
            'all_case_sum': all_case['len'],  # int
            'success_case_sum': success['len'],  # int
            'errors_case_sum': errors['len'],  # int
            'skipped_case_sum': skipped['len'],  # int
        }
        # html
        data['chart_html'] = self.__get_cases_chart_html(data)
        # html
        data['nav_html'] = self.__get_cases_nav_html(data)
        case_info = [
            {'name': 'all_cases', 'list': all_case['cases']},
            {'name': 'success_cases', 'list': success['cases']},
            {'name': 'errors_cases', 'list': errors['cases']},
            {'name': 'skipped_cases', 'list': skipped['cases']}
        ]
        content_html = self.get_cases_content_html(case_info)
        data['content_html'] = content_html

        return data

    def __send_mail(self, data):
        receivers = self.yaml_repore.get('receivers')
        subject = self.yaml_repore.get('title')
        host = self.yaml_repore.get('server.host')
        port = self.yaml_repore.get('server.port')

        # 获取mail_html路径
        html_path = os.path.dirname(__file__) + '/tpl/mail_html.txt'
        # 基础模板文件
        html_code = Utils.open_file(html_path)
        # 邮件发送内容
        content = Template(html_code).render({
            "title": subject,
            "all_case_sum": data['all_case_sum'],
            "success_case_sum": data['success_case_sum'],
            "errors_case_sum": data['errors_case_sum'],
            "skipped_case_sum": data['skipped_case_sum'],
            "report_path": str(host) + ':' + str(port) + '/report.html'
        })
        # 发送邮件
        self._mail.send(receivers, subject, content)

    def build(self):
        get_data = self.get_output_field_data()

        # 获取template路径
        code_path = os.path.dirname(__file__) + '/tpl/template.html'
        # 基础模板文件
        template_html = Utils.open_file(code_path)
        html = Template(template_html).render(get_data)
        # 写入内容
        Utils.write_file(self.report_html_path, html)
        # 发送邮件
        if self.yaml_config.get('reportSendMail') is True:
            self.__send_mail(get_data)


if __name__ == '__main__':
    demo = [{'status_type': 'success', 'name': '登录', 'url': 'http://139.196.192.35:39001/api/login', 'mode': 'post',
             'submit_data': {'name': 15000000000, 'password': 123}, 'code': 200, 'status': 'success',
             'data': {'status': 'success', 'msg': '登录成功，一般成功后不会有msg提示', 'data': 'token:123456'}, 'time': 0.108004,
             'msg': ''},
            {'status_type': 'error', 'name': '登录', 'url': 'http://139.196.192.35:39001/api/reg', 'mode': 'post',
             'submit_data': {'name': 15000000000, 'password': 123}, 'code': 404, 'status': 'error', 'data': {},
             'time': 0.166182, 'msg': ''},
            {'status_type': 'success', 'name': '获取所有用户', 'url': 'http://139.196.192.35:39001/api/get_users',
             'mode': 'get', 'submit_data': {}, 'code': 200, 'status': 'success',
             'data': {'status': 'success', 'data': ['1111', '2222', '3333', '4444', '5555']}, 'time': 0.195988,
             'msg': ''},
            {'status_type': 'success', 'name': '获取所有用户', 'url': 'http://139.196.192.35:39001/api/get_users',
             'mode': 'get', 'submit_data': {}, 'code': 200, 'status': 'success',
             'data': {'status': 'success', 'data': ['1111', '2222', '3333', '4444', '5555']}, 'time': 0.195988,
             'msg': ''}]

    ReporeHtml(0, 0, demo).build()

    # 使用浏览器打开html
    # webbrowser.open("test_demo.html")

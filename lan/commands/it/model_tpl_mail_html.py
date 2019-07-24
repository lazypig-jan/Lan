content = '''
<h1>{{title}}</h1>
<p>所有用例：{{all_case_sum}}</p>
<p>成功用例：{{success_case_sum}}</p>
<p>失败用例：{{errors_case_sum}}</p>
<p>跳过用例：{{skipped_case_sum}}</p>
<p><a href="{{report_path}}">报告</a></p>
'''


def get_maile_html_tpl():
    return content


if __name__ == '__main__':
    print(get_maile_html_tpl())

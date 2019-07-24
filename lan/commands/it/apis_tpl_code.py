content = '''
# coding=utf-8
import unittest2
from lan import Request, Log
from model import Test

class {{ClassName}}(Test):
    {% for item in funs %}
    # {{item.data.name}}
    def {{item.name}}(self):
    {% if item.data.mode == "post" %}
        self.result = Request.post(self.data['url'], data=self.data['data'], token=False)
    {% else %}
        self.result = Request.get(self.data['url'])
    {% endif %}
        self.assertEqual(1, 1)
    {% endfor %}

# 运行
if __name__ == '__main__':
    unittest2.main()
'''


def get_apis_code_tpl():
    return content


if __name__ == '__main__':
    print(get_apis_code_tpl())

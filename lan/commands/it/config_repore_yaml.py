content = '''
# 测试报告配置
#访问报告域名
server:
  host: http://127.0.0.1 # www.uihtml.com/192.168.0.1
  port: 80
# 标题
title: 接口自动化测试报告
# 接收者
receivers: 643826784@qq.com
# 状态类型输出
cases:
  all: 全部
  success: 成功
  error: 错误
  skip: 跳过
# 表格输出
table:
  case_id: 用例编号
  case_name: 用例名称
  api_url: 接口地址
  method: 接口方法
  time: 时间
  result: 测试结果
  detailed: 详细信息
'''


def get_config_repore_tpl():
    return content


if __name__ == '__main__':
    print(get_config_repore_tpl())

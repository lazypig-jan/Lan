content = '''
# 响应处理-可为空 如果为空就不判断响应后的字段
response:
  # 状态字段 一般是code 或者 status
  status_field: status
  # 状态字段 正确 值
  status_success_val: success
  # 错误提示字段
  error_field: msg
'''


def get_config_response_tpl():
    return content


if __name__ == '__main__':
    print(get_config_response_tpl())

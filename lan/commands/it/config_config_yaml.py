content = '''
# 当前项目配置文件

# 域名
domain: http://139.196.192.35:39001
# 中断继续
interruptContinue: True
# 报告是否发送邮件
reportSendMail: False
'''


def get_config_config_tpl():
    return content


if __name__ == '__main__':
    print(get_config_config_tpl())

content = '''
# 邮箱服务配置
host: smtp.qq.com
port: 465
user: admin@qq.com
passwd: 123456
'''


def get_config_mail_tpl():
    return content


if __name__ == '__main__':
    print(get_config_mail_tpl())

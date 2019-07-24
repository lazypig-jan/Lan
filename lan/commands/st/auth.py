# coding=utf-8

from lan import Request, Log, Config


class Auth(object):
    def __init__(self):
        self.ini = Config(name='Token', section='config')
        # 获取ini下的域名
        self.api = self.ini.get('domain')

        self.name = 'bobby'
        self.password = '123456789'

    def login(self):
        # 控制台输入模式
        # self.name = input('请输入用户名：')
        # self.password = input('请输入密码：')

        r = Request.post(self.api + '/api/login', {
            'name': self.name,
            'password': self.password
        })

        if r['status_code'] == 200:
            self.ini.set('token', r['response']['token'])


if __name__ == '__main__':
    Auth.login()

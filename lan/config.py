
import os
import configparser
from lan.utils import Utils
from lan.log import Log


class Config:
    def __init__(self, path='./', name='config', section='CONFIG'):
        # 获取根目录下config.ini
        self.config_path = os.path.join(path, name + '.ini')
        # 读取配置文件
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path, 'utf-8')
        # 获取section
        self.section = section
        # 判断是否有ini文件 没有就创建
        if os.path.exists(self.config_path) is False:
            self.config.add_section(section)
            Log.debug('创建' + name + '.ini')

    def get(self, name=''):
        """
        获取值
        """
        if Utils.empty(name):
            Log.error('name不能为空')
            return False

        # 获取config
        val = self.config.get(self.section, name)
        return val

    def set(self, name="", value=""):
        """
        给ini设置值
        """
        self.config.set(self.section, name, value)
        # 写入配置文件
        self.config.write(open(self.config_path, "w"))


if __name__ == '__main__':
    c = Config(
        path='./',
        name='Token',
        section='USER'
    )
    c.set('user', '1234')
    c.set('psw', '1233')
    Log.debug('user:' + c.get('user'))

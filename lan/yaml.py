import warnings, yaml
from lan.log import Log


class Yaml(object):
    def __init__(self, path='./', file_name="config"):
        """
        初始化
        """
        # 忽略掉yaml告警
        warnings.simplefilter("ignore", DeprecationWarning)

        # 每个项目下面有个config.yaml
        config_path = path + '/' + file_name + '.yaml'
        # yaml的读取
        f = open(config_path, encoding='utf-8')
        self.data = yaml.safe_load(f)
        f.close()

    def get(self, name=''):
        _data = self.data
        """
        获取yaml
        """
        if name != '':
            try:
                for item in name.split('.'):
                    _data = _data[item]
            except Exception as e:
                _data = ''
        return _data


if __name__ == '__main__':
    y = Yaml('./')
    name = y.get('name')
    Log.debug(name)

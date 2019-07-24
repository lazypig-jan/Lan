from tinydb import TinyDB, where
from .utils import Utils


class FileDb:
    """
    Json文件db
    """

    def __init__(self, path='', name=''):
        if Utils.empty(path):
            print('请输入保存路径')
            return False
        """
        初始化 获取db文件路径
        """
        self.db_path = path + '/' + name + '.json'

    def _db(self):
        """
        TinyDB实例化
        """
        return TinyDB(self.db_path)

    def inster(self, data):
        """
        插入数据
        {'a':1}
        """
        return self._db().insert(data)

    def inster_all(self, data):
        """
        插入多条
        """
        return self._db().insert_multiple(data)

    def select(self):
        """
        查询所有
        """
        return self._db().all()

    def find(self, key="", val=""):
        """
        查询单条
        """
        return self._db().get(where(key) == val)

    def remove(self):
        """
        删除
        """
        Utils.remove_file(self.db_path)


if __name__ == '__main__':
    print('测试db')
    FileDb().inster({
        'status': 1,
        'method_name': 2
    })
    # FileDb().remove_db()

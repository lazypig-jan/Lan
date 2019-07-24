import os
from lan import Log


def run(args=None):
    path = os.getcwd() + '/run.py'

    is_exists = os.path.exists(path)

    if not is_exists:
        # 如果不存在则创建目录
        Log.debug("当前目录没有run.py文件，请进入正确目录")
    else:
        # 如果目录存在则不创建，并提示目录已存在
        os.system("python3 " + path)


if __name__ == '__main__':
    print(os.environ)

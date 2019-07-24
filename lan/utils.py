import os, datetime, time


class Utils(object):
    @staticmethod
    def get_time(timestamp):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

    @staticmethod
    def time_ymd():
        """
        获取年月日
        """
        y = datetime.datetime.now().year
        m = datetime.datetime.now().month
        d = datetime.datetime.now().day
        return str(y) + str(m) + str(d)

    @staticmethod
    def empty(val):
        """
        判断是否为空
        """
        if val == None or val == '' or val == 'null':
            return True
        else:
            return False

    @staticmethod
    def mkdir(path):
        """
        创建目录
        """
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")

        """
        判断路径是否存在
        存在     True
        不存在   False
        """
        is_exists = os.path.exists(path)

        if not is_exists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            # print(path+' 目录已存在')
            return False

    @staticmethod
    def open_file(path):
        """
        读取文件
        """
        file_object = open(path, 'r', encoding='utf-8')
        try:
            ftext = file_object.read()
        finally:
            file_object.close()

        return ftext

    @staticmethod
    def write_file(path, content=''):
        """
        写入文件
        """
        if os.path.exists(path) is False:
            file = open(path, 'w', encoding='utf-8')
            file.write(content)
            file.close()

    @staticmethod
    def remove_file(path):
        """
        删除文件
        """
        if os.path.exists(path) is True:
            os.remove(path)


if __name__ == '__main__':
    print(Utils.time_ymd())

import logzero
from logzero import logger
from lan.utils import Utils


class Log(object):
    def __init__(self, path='./log/', name='log', logfile=False):
        if Utils.empty(path):
            print('请输入保存路径')
            return False
        # 配置文件 是否生成log文件
        if logfile:
            logzero.logfile(path + "/" + Utils.time_ymd() + "_" + name + ".log", maxBytes=1e6, backupCount=1)

    @staticmethod
    def info(content):
        logger.info(content)

    @staticmethod
    def debug(content):
        logger.debug(content)

    @staticmethod
    def warning(content):
        logger.warning(content)

    @staticmethod
    def error(content):
        logger.error(content)


if __name__ == '__main__':
    print('测试日志')
    Log.debug('测试debug')
    Log.info('测试info')
    Log.warning('测试warning')
    Log.error('测试error')

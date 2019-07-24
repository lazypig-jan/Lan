# -*- coding: UTF-8 -*-
from lan.config import Config
from lan.utils import Utils
from lan.log import Log
from lan.commands.pub import mkdir, tpl, init_file


def server(args=None):
    if None is args:
        Log.error('没有name参数')
        return False

    Log.debug(args)


if __name__ == '__main__':
    server()

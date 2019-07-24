from lan.log import Log
from lan.commands.it import it
from lan.commands.st import st
from lan.commands.sm import sm


def create(args=None):
    if None is args:
        Log.error('没有name参数')
        return False
    name = args.name.split("/", 1)
    # name = ["it", "demo"]
    if name[0] == "it":
        it(name[1])
    elif name[0] == "st":
        st(name[1])
    elif name[0] == "sm":
        sm()
    else:
        Log.debug("没有相关类型 请输入it/project st/project sm/project")


if __name__ == '__main__':
    create()

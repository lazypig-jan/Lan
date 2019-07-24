
import argparse
from lan.commands.create import create
from lan.commands.make import make
from lan.commands.run import run
from lan.commands.server import server


def main():
    parser = argparse.ArgumentParser(prog='lan', description="Lan(懒)是一套Python测试套件脚手架")
    subparsers = parser.add_subparsers()

    parser_it = subparsers.add_parser('create', help='- 创建项目 项目类型(it st sm)/项目名称')
    parser_it.add_argument('name', help='- 请输入项目类型(it st sm)/项目名称')
    parser_it.set_defaults(func=create)

    parser_st = subparsers.add_parser('make', help='- 用例生成 根据config.yaml文件生成用例文件')
    parser_st.set_defaults(func=make)

    parser_st = subparsers.add_parser('run', help='- 运行项目 结束退出')
    parser_st.set_defaults(func=run)

    parser_st = subparsers.add_parser('server', help='- 运行项目 后台模式')
    parser_st.set_defaults(func=server)

    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.print_help()


if __name__ == '__main__':
    main()

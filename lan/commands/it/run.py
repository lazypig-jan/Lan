import os
from model.testrunner import TestRunner

# 测试入口
TestRunner(os.getcwd()).run()
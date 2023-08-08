# -*- coding: utf-8 -*-
import logging

# 配置输出格式和输出级别
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    filename='test.log',
                    filemode='a')

"""
%(name)s：Logger的名字
%(levelno)s：打印日志级别的数值
%(levelname)s：打印日志级别的名称
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s：打印当前执行程序名
%(funcName)s：打印日志的当前函数
%(lineno)d：打印日志的当前行号
%(asctime)s：打印日志的时间
%(thread)d：打印线程ID
%(threadName)s：打印线程名称
%(process)d：打印进程ID
%(message)s：打印日志信息
"""


# 日志级别
logging.debug('debug级别，一般用来打印一些调试信息，级别最低')
logging.info('info级别，一般用来打印一些正常的操作信息')
logging.warning('waring级别，一般用来打印警告信息')
# logging.error('error级别，一般用来打印一些错误信息')
# logging.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')










# -*- coding: utf-8 -*-

import datetime
from typing import Callable
import time

time_record_commands = ['start_time = time.time()',
                        'end_time = time.time()',
                        "print(f'used time: {end_time-start_time}s')"]


def date_time_demo():
    now = datetime.datetime.now()
    print(f"Time at Present: {now.strftime('%Y-%m-%d %H:%M:%S')}")


def time_commands_demo():
    exec(time_record_commands[0])
    exec(time_record_commands[1])
    eval(time_record_commands[2])


def timing(func: Callable):
    def record_decorator(*args, **kwargs):
        start_time = time.time()

        decorated_func = func(*args, **kwargs)

        end_time = time.time()
        print(f'used time: {end_time-start_time}s')
        return decorated_func

    return record_decorator


def record_time(func: Callable):
    def record_decorator(*args, **kwargs):
        now = datetime.datetime.now()
        print(f'started@' + now.strftime('%Y-%m-%d %H:%M:%S'))

        decorated_func = func(*args, **kwargs)

        now = datetime.datetime.now()
        print(f'done@' + now.strftime('%Y-%m-%d %H:%M:%S'))
        return decorated_func

    return record_decorator


if __name__ == '__main__':
    # @record_time
    # @timing
    # def func(a: int):
    #     return a

    # s = func(a=10)
    date_time_demo()
    time_commands_demo()

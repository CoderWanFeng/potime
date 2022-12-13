#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: 图片.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 时间 的自动化操作
#############################################

import time


def RunTime(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f"function：【{func.__name__}】,runtime：【{str(t2 - t1)}】s")
        return res

    return wrapper

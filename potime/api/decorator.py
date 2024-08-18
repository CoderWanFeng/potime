

import time


def RunTime(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f"function：【{func.__name__}】,runtime：【{str(t2 - t1)}】s")
        return res

    return wrapper

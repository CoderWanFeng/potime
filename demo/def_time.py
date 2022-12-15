# pip install potime
from potime import RunTime

@RunTime
def add_sum(start, end):
    if start <= end:
        res = sum(range(start, end + 1))
        print(res)
    else:
        print('计算范围不正确：起点大于终点')


if __name__ == '__main__':
    start = 1
    end = 1 * 10000 * 10000
    add_sum(start, end)

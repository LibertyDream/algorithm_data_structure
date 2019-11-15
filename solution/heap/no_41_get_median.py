'''面试题41：数据流中的中位数

设法得到一个数据流中的中位数
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''

import heapq as hq

class DynamicFlow(object):

    def __init__(self):
        self.__max = []
        self.__min = []
        self.__size = 0
    
    def insert(self, item):

        if self.__size & 1 == 0:
            if len(self.__max) > 0 and self.__max[0] > item:
                hq.heappush(self.__max, item)
                item = hq.heappop(self.__max)

            hq.heappush(self.__min, item)
        else:
            if len(self.__min) > 0 and self.__min[0] < item:
                hq.heappush(self.__min, item)
                item = hq.heappop(self.__min)

            hq.heappush(self.__max, item)
        self.__size += 1
    
    def get_median(self):

        if self.__size == 0:
            raise ValueError('cannot get median from empty flow')

        if self.__size & 1 == 0:
            left = hq.heappop(self.__max)
            right = hq.heappop(self.__min)
            return left + (right - left) / 2
        else:
            return hq.heappop(self.__min)
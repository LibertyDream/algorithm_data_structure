'''面试题53-2：0~n-1中缺失的数字

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0~n-1之内。
在范围0~n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
'''
import random

def get_missing_num(arr):

    if arr is None or len(arr) == 0:
        return -1

    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + ((end - start) >> 1)

        if arr[mid] == mid:
            start = mid + 1
        else:
            if mid > 0 and arr[mid - 1] != mid - 1:
                end = mid - 1
            else:
                return mid
    if start == len(arr):
        return len(arr)
    return -1

if __name__ == "__main__":

    n = 8
    
    datas = [[],None,[0]]
    for _ in range(n):

        del_num = random.randint(0, n-1)
        data = [x for x in range(n) if x != del_num]
        datas.append(data)
    
    for data in datas:
        print(data, get_missing_num(data))
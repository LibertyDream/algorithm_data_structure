'''面试题39：数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
-------------
Example:
input:[1，2，3，2，2，2，5，4，2]
output:2
'''
import random

def __partition(array, begin, end):
    if begin >= end:
        return begin
    idx = random.randint(begin, end)
    array[begin], array[idx] = array[idx], array[begin]

    lt = begin
    gt = end + 1
    idx = begin + 1
    while idx != gt:
        if array[idx] < array[begin]:
            lt += 1
            array[idx], array[lt] = array[lt], array[idx]
            idx += 1
        elif array[idx] > array[begin]:
            gt -= 1
            array[idx], array[gt] = array[gt], array[idx]
        else:
            idx += 1

    array[begin], array[lt] = array[lt], array[begin]
    
    return lt

def more_than_half_partition(array):
    if array is None or len(array) <= 0:
        return None

    mid = len(array) // 2
    begin = 0
    end = len(array)-1

    index = __partition(array, begin, end)
   
    while index != mid:
        if index > mid:
            end = index - 1
            index = __partition(array, begin, end)
        elif index < mid:
            begin = index + 1
            index = __partition(array, begin, end)
    
    num = array[index]
    times = 0
    for i in array:
        if i == num:
            times += 1
    
    if times * 2 > len(array):
        return array[index]
    
    return None

def more_than_half_scan(array):

    if array is None or len(array) <= 0:
        return None

    times = 1
    cur = array[0]
    for i in range(1,len(array)):
        if cur == array[i]:
            times += 1
        elif times == 0:
            cur = array[i]
            times = 1
        else:
            times -= 1
    
    times = 0
    for i in range(len(array)):
        if cur == array[i]:
            times += 1

    if times * 2 > len(array):
        return cur
    return None
        
if __name__ == "__main__":

    datas = [[1,2,3,2,2,2,5,4,2],[1,2,2,4,5,6,7,8],None,[]]

    for data in datas:
        print(more_than_half_partition(data))
        print(more_than_half_scan(data))
'''题目三-2：不修改数组找出重复的数字。

在一个长度为n+l的数组里的所有数字都在1～n的范围内，所以数组中至少有一个数字是重复的。
请找出数组中任意一个重复的数字，但不能修改输入的数组。
-------
Example:
input:[2，3，5，4，3，2，6，7]
output: 2 or 3
--------
注意交流，问清功能需求（任意一个重复数字还是所有重复数字）和效率需求（时间优先，空间优先）
'''

def duplicate(arr:list)-> int:

    if arr is None:
        return -1

    if len(arr) == 0:
        return -1

    for x in arr:
        if x < 1 or x > len(arr) - 1:
            return -1

    start = 1
    end = len(arr) - 1
    while end >= start:

        mid = start + (end - start) // 2
        counts = __count_num(arr, start, mid)
        if counts > (mid - start + 1):
            if start == end:
                return start
            end = mid
        else:
            start = mid + 1
    print(start, end)
    return -1

def __count_num(arr, start,end):

    if arr is None:
        return -1

    count = 0

    for x in arr:
        if x >= start and x <= end:
            count += 1
    
    return count
    

if __name__ == "__main__":
    
    arr = []
    arr1 = None
    arr2 = [2,3,5,4,8,2,6,7]
    arr3 = [2,3,5,4,3,2,6,7]

    print(duplicate(arr))
    print(duplicate(arr1))
    print(duplicate(arr2))
    print(duplicate(arr3))
    
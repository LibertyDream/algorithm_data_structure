'''题目三-1：找出数组中重复的数字。
    
在一个长度为n的数组里的所有数字都在 0~n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
-------
Example:
input:[2，3，1，0，2，5，3]
output: 2 or 3
'''

def duplicate(arr:list)-> int:

    if arr is None:
        return -1

    if len(arr) == 0:
        return -1

    for x in arr:
        if x < 0 or x >= len(arr):
            return -1

    for i in range(len(arr)):

        while arr[i] != i:
            if arr[i] == arr[arr[i]]:
                return arr[i]
            temp = arr[i]
            arr[i], arr[temp] = arr[temp], arr[i]
    
    return -1

if __name__ == "__main__":

    arr = []
    arr2 = [2,3,-1,0,4]
    arr3 = [2,3,1,0,2,5,3]


    print(duplicate(arr))
    print(duplicate(arr2))
    print(duplicate(arr3))
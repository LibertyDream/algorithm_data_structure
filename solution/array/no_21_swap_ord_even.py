'''面试题21：调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，
所有偶数位于数组的后半部分。
------------
Example
input:[1,2,3,4,5]
output:[1,5,3,4,2]
'''

def reorder(arr, func):

    if arr is None:
        return None
    
    pre = 0
    post = len(arr) - 1
    while pre < post:

        while pre < len(arr) and not func(arr[pre]):
            pre = pre + 1
        
        while post > -1 and func(arr[post]):
            post = post - 1

        if pre < post:
            arr[pre], arr[post] = arr[post], arr[pre]
    
    return arr

def is_even(num):

    return num & 1 == 0

if __name__ == "__main__":

    data1 = [1,2,3,4,5,6]
    data2 = [1,3,5,7,2,4,6]
    data3 = [2,4,6,8,1,3,5]
    data4 = [3]
    data5 = []

    print(data1,reorder(data1,is_even))
    print(data2,reorder(data2,is_even))
    print(data3,reorder(data3,is_even))
    print(data4,reorder(data4,is_even))
    print(data5,reorder(data5,is_even))
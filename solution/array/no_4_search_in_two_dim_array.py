'''面试题4：二维数组中的查找

在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
-------------------
Example：
input:
[    [1,2,8,9],
    [2,4,9,12],
    [4,7,10,13],
    [6,8,11,15]    ], 7
output: True
----------------------
一旦有了顺序性，二分与边界值就可以用起来了
'''

def contain(arr, num):

    if arr is None or not isinstance(num, int):
        return False
    
    rows = len(arr)
    columns = len(arr[0])
    
    if arr[0][0] > num or arr[rows - 1][columns - 1] < num:
        return False

    row = 0
    column = columns - 1

    while row < rows and column > 0:

        cur = arr[row][column]
        if cur == num:
            return True
        elif cur > num:
            column -= 1
        else:
            row += 1
    
    return False

if __name__ == "__main__":
    data = [[1,2,8,9],
    [2,4,9,12],
    [4,7,10,13],
    [6,8,11,15]]


    query1 = 0
    query2 = 16
    query3 = 3
    query4 = 7

    print(contain(None,None))
    print(contain(data,None))
    print(contain(data,query1))
    print(contain(data,query2))
    print(contain(data,query3))
    print(contain(data,query4))
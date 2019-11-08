'''面试题29：顺时针打印矩阵

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
--------------
Example:
input:
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16
output:1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
'''

def print_array_clockwise(array):

    if array is None or len(array) == 0:
        return

    rows = len(array)
    cols = len(array[0])
    
    if cols == 0:
        print()
        return
    
    start = 0
    while rows > 2 * start and cols > start * 2:
        __clockwise_print(array, rows, cols, start)
        start = start + 1

def __clockwise_print(array, rows, cols, start):

    end_row = rows - 1 - start
    end_col = cols - 1 - start

    for x in range(start, end_col + 1):
        
        print(array[start][x], end = ' ')

    if end_row > start:
        for x in range(start + 1, end_row + 1):
            print(array[x][end_col], end = ' ')
    
    if end_row > start and end_col > start:
       x = end_col - 1
       while x > start - 1:
            print(array[end_row][x], end = ' ')
            x -= 1

    
    if start < end_col and end_row - 1 > start:
        x = end_row - 1
        while x != start:
            print(array[x][start], end = ' ')
            x -= 1

def __get_matrix(rows, cols):

    ret = []
    count = 0
    for i in range(rows):
        temp = []
        for j in range(cols):
            count += 1
            temp.append(count)
        ret.append(temp)
    return ret

def __print_matrix(arr):

    for x in arr:
        for y in x:
            if y < 10:
                print(' '+str(y), end=' ')
            else:
                print(y,end=' ')
        print()

if __name__ == '__main__':

    matrix = __get_matrix(1,1)
    __print_matrix(matrix)
    print_array_clockwise(matrix)
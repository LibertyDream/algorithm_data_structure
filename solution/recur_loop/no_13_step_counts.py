'''面试题13：机器人的运动范围

地上有一个m行n列的方格。一个机器人从坐标（0，0）的格子开始移动，
它每次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35，37），因为3+5+3+7=18。
但它不能进入方格（35，38），因为3+5+3+8=19。请问该机器人能够到达多少个格子？
'''

def cell_counts(m, n, k):

    if m <= 0 or n <= 0 or k <= 0:
        return 0

    visited = []
    for i in range(m):
        visited.append([False]*n)

    return __cell_counts(m,n,k,0,0,visited)

def __cell_counts(rows, cols,limit, row, col, visited):

    if row < 0 or row >= rows or col < 0 or col >= cols:
        return 0
    counts = 0
    if __checked(rows, cols, limit, row, col, visited):
        counts += 1
        visited[row][col] = True
        counts += (__cell_counts(rows, cols,limit, row - 1, col, visited) + 
            __cell_counts(rows, cols,limit, row + 1, col, visited) +
            __cell_counts(rows, cols,limit, row, col - 1, visited) +
            __cell_counts(rows, cols,limit, row, col + 1, visited))
    
    return counts

def __checked(rows, cols, limit, row, col, visited):

    if (row >= 0 and row < rows and col >= 0 and col < cols 
    and not visited[row][col] and __is_legal(limit, row,col)):
        return True
    return False

def __is_legal(limit, row, col):
    total = 0
    while row > 0:
        total += row % 10
        row //= 10
    while col > 0:
        total += col % 10
        col //= 10
    
    if total > limit:
        return False
    return True

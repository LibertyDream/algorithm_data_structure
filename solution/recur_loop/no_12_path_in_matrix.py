'''面试题12：矩阵中的路径

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
-----------
Example:

a,b,t,g
c,f,c,s
j,d,e,h

input:'bfce'
output:True

input:'abfb'
output:False
'''

def has_path(matrix, string):

    
    if matrix is None or string is None:
        return False

    visited = [[]] * len(matrix)
    for i in range(len(visited)):
        x = [False] * len(matrix[0])
        visited[i] = x
    length = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if __has_path(matrix, length, string, i, j, visited):
                return True
    
    return False

def __has_path(matrix, length, string, cow, low, visited):

    if length == len(string):
        return True
    
    ret = False
    if (cow >= 0 and cow < len(matrix) and low >= 0 and low < len(matrix[0]) 
    and matrix[cow][low] == string[length] and not visited[cow][low]):
        length += 1
        visited[cow][low] = True
        ret = (__has_path(matrix, length, string, cow - 1, low, visited)
            or __has_path(matrix, length, string, cow + 1, low, visited)
            or __has_path(matrix, length, string, cow, low - 1, visited)
            or __has_path(matrix, length, string, cow, low + 1, visited))
        
        if not ret:
            length -= 1
            visited[cow][low] = False

    return ret


if __name__ == "__main__":

    datas = [['a','b','t','g'],
        ['c','f','c','s'],
        ['j','d','e','h']]

    print(has_path(None,None))
    print(has_path([],'bfce'))
    print(has_path(datas, 'bfce'))
    print(has_path(datas, 'abfb'))

    data1 = [['a','b','t','g']]

    print(has_path(data1, 'abt'))
    print(has_path(data1, 'bab'))

'''面试题47：礼物的最大价值

在一个mxn的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格，直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？
'''

def max_gift_value(arr):

    if arr is None or len(arr) == 0 or len(arr[0]) == 0:
        return 0

    rows = len(arr)
    cols = len(arr[0])

    values = [0] * cols

    for i in range(rows):
        for j in range(cols):
            up = 0
            left = 0

            if i > 0:
                up = values[j]
            if j > 0:
                left = values[j-1]
            
            values[j] = max(up, left) + arr[i][j]
    
    return values[cols-1]

if __name__ == '__main__':

    gift = [[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]
    print(max_gift_value(gift))
    print(max_gift_value(None))
    print(max_gift_value([[1]]))
    print(max_gift_value([[1,2,3,4,5]]))
    print(max_gift_value([[2],[3],[4],[5]]))
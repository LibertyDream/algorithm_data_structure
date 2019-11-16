'''面试题59：滑动窗口的最大值

给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。
------------
input:[2，3，4，2，6，2，5，1] 3
output:[4，4，6，6，6，5]
'''
from collections import deque

def max_in_window(arr, size):

    if arr is None or len(arr) == 0 or size <= 0:
        return None

    dq = deque()
    ret = []
    for i in range(size):
        while len(dq) > 0 and arr[i] > arr[dq[-1]]:
            dq.pop()
        dq.append(i)

    for i in range(size, len(arr)):
        ret.append(arr[dq[0]])

        while len(dq) > 0 and arr[i] > arr[dq[-1]]:
            dq.pop()
        
        if len(dq)> 0 and dq[0] <= i - size:
            dq.popleft()

        dq.append(i)

    ret.append(arr[dq[0]])
    return ret
        
if __name__ == '__main__':

    data = [2,3,4,2,6,2,5,1]
    print(max_in_window(data, 3))
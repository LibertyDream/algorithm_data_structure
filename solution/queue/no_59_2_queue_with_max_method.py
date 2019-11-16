'''面试题59-2:队列的最大值

请定义一个队列并实现函数max得到队列里的最大值，
要求函数max、push_back和pop_front的时间复杂度都是O（1）。
'''
from collections import deque

class Node(object):

    def __init__(self, idx, value):
        self.idx = idx
        self.value = value

class Queue(object):

    def __init__(self):
        self.data = deque()
        self.max = deque()
        self.idx = 0

    def push_back(self, data):

        while len(self.max) > 0 and self.max[-1].value < data:
            self.max.pop()

        self.data.append(Node(self.idx, data))
        self.max.append(Node(self.idx, data))
        self.idx += 1

    def pop_front(self):

        if len(self.max) > 0 and self.max[0].idx == self.data[0].idx:
            self.max.popleft()
        
        return self.data.popleft().value
    
    def max(self):

        if len(self.max) > 0:
            return self.max[0].value


        


if __name__ == "__main__":

    dq = deque()
    dq.append(1)
    dq.append(2)
    print(dq[-1])
    
    
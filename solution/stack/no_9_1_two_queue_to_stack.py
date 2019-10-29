'''面试题9-1：用两个队列实现栈

用两个队列实现一个栈。实现队列中的两个方法push和pop，
分别完成在栈顶压入和弹出元素的操作。
'''

from collections import deque

class Stack(object):

    def __init__(self):
        self.__queue1 = deque()
        self.__queue2 = deque()
        self.size = 0

    def push(self, ele):
        
        if ele is None:
            return
        self.__queue1.append(ele)
        self.size += 1
    
    def pop(self):
        ret = None
        if len(self.__queue1) == 0:
            if len(self.__queue2) == 0:
                raise ValueError('Stack is empty')
            for _ in range(len(self.__queue2) - 1):
                self.__queue1.append(self.__queue2.popleft())
            ret = self.__queue2.popleft()
        else:
            for _ in range(len(self.__queue1) - 1):
                self.__queue2.append(self.__queue1.popleft())    
            ret = self.__queue1.popleft()
        self.size -= 1
        return ret

if __name__ == '__main__':

    stack =Stack()

    stack.push(1)
    print(stack.pop())

    # stack.pop()

    data = [1,2,3]
    for x in data:
        stack.push(x)
    for i in range(stack.size):
        print(stack.pop(), end = ' ')
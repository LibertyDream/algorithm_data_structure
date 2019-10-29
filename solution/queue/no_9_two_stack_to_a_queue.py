'''面试题9：用两个栈实现队列

用两个栈实现一个队列。实现队列中的两个函数appendTail和deleteHead，
分别完成在队列尾部插入节点和在队列头部删除节点的功能。
'''

class Queue(object):

    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []
        self.size = 0
    
    def appendTail(self, ele):

        if ele is None:
            return
        self.size += 1
        self.__stack1.append(ele)
    
    def deleteHead(self):

        ret = None
        if len(self.__stack2) == 0:
            if len(self.__stack1) == 0:
                raise ValueError('Empty queue')
            for i in range(len(self.__stack1)):
                self.__stack2.append(self.__stack1.pop())
            
        ret = self.__stack2.pop()
        self.size -= 1

        return ret
            

if __name__ == "__main__":

    data = [1,2,3]

    queue = Queue()

    queue.appendTail(1)
    print(queue.deleteHead())

    # queue.deleteHead()


    for x in data:
        queue.appendTail(x)
    for i in range(queue.size):
        print(queue.deleteHead(), end=' ')

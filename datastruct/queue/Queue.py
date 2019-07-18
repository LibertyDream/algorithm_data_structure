from abc import ABCMeta, abstractmethod

'''
    借助抽象类定义Queue接口形态
'''


class Queue(metaclass=ABCMeta):

    #  入队
    @abstractmethod
    def enqueue(self, ele):
        pass

    #  出队
    @abstractmethod
    def dequeue(self):
        pass

    #  队列元素个数
    @abstractmethod
    def get_size(self):
        pass

    #  返回队首元素
    @abstractmethod
    def get_front(self):
        pass

    #  队列是否为空
    @abstractmethod
    def is_empty(self):
        pass


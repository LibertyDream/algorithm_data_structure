from abc import ABCMeta, abstractmethod

'''
    借助抽象类实现接口，定义栈的主要方法
'''

class Stack(metaclass=ABCMeta):

    # 出栈
    @abstractmethod
    def pop(self):
        pass

    # 查看栈顶元素
    @abstractmethod
    def peek(self):
        pass

    # 获取栈内元素个数
    @abstractmethod
    def get_size(self):
        pass

    # 入栈
    @abstractmethod
    def push(self, ele):
        pass

    # 栈是否为空
    @abstractmethod
    def is_empty(self):
        pass
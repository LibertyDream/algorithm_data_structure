from Array import Array
from Stack import Stack

class ArrayStack(Stack):
    def __init__(self, capacity: int = 10):
        self.__data = Array(capacity)

    def peek(self):
        return self.__data.get_last()

    def push(self, ele):
        self.__data.add_to_last(ele)

    def get_size(self):
        return self.__data.get_size()

    def pop(self):
        return self.__data.remove_last()

    def is_empty(self):
        return self.__data.is_empty()

    def __str__(self):
        bstr = 'ArrayStack size: %d, capacity: %d\n' % (self.__data.get_size(), self.__data.get_capacity())
        bstr += '['
        for i in range(self.__data.get_size()):
            bstr += '' + str(self.__data.get(i))
            if i != self.__data.get_size() - 1:
                bstr += ', '
        bstr += '] top'
        return bstr

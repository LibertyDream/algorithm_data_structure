from Array import Array
from Queue import Queue


class ArrayQueue(Queue):

    def __init__(self, capacity: int = 10):
        self.__data = Array(capacity)

    def get_size(self):
        return self.__data.get_size()

    def enqueue(self, ele):
        self.__data.add_to_last(ele)

    def is_empty(self):
        return self.__data.is_empty()

    def dequeue(self):
        return self.__data.remove_first()

    def get_front(self):
        return self.__data.get_first()

    def get_capacity(self):
        return self.__data.get_capacity()

    def __str__(self):
        bstr = 'ArrayQueue size: %d, capacity: %d\n' % (self.__data.get_size(), self.__data.get_capacity())
        bstr += 'front ['
        for i in range(self.__data.get_size()):
            bstr += '' + str(self.__data.get(i))
            if i != self.__data.get_size() - 1:
                bstr += ', '
        bstr += '] tail'
        return bstr

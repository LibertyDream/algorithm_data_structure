from Queue import Queue
from MaxHeap import MaxHeap

class PriorityQueue(Queue):

    def __init__(self):
        self.__max_heap = MaxHeap()
    
    def get_size(self):
        return self.__max_heap.get_size()
    
    def is_empty(self):
        return self.__max_heap.is_empty()

    def enqueue(self, ele):
        self.__max_heap.add(ele)
    
    def get_front(self):
        return self.__max_heap.get_max()

    def dequeue(self):
        return self.__max_heap.extract_max()

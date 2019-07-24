from Queue import Queue

class Node(object):
    def __init__(self, ele = None, next_node = None):
        self.data = ele
        self.next = next_node
    
    def __str__(self):
        return str(self.data)

class LinkedListQueue(Queue):
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def is_empty(self):
        return self.__size == 0
    
    def get_size(self):
        return self.__size

    def enqueue(self, ele):
        if self.__tail == None:
            self.__tail = Node(ele)
            self.__head = self.__tail
        else:
            self.__tail.next = Node(ele)
            self.__tail = self.__tail.next
        self.__size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Cannot dequeue from an empty queue!')

        cur = self.__head
        self.__head = self.__head.next
        cur.next = Node

        if self.__head == None:
            self.__tail = None
        
        self.__size -= 1

        return cur.data
    
    def get_front(self):
        return self.__head.data
    
    def __str__(self):
        string = 'front '
        cur = self.__head

        while cur != None:
            string += str(cur) + '->'
            cur = cur.next
        string += 'null tail'
        return string

    


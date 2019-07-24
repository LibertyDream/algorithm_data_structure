from LinkedList import LinkedList
from Stack import Stack

class LinkedListStack(Stack):
    def __init__(self):
        self.__list = LinkedList()
    
    def get_size(self):
        return self.__list.get_size()
    
    def is_empty(self):
        return self.__list.is_empty()
    
    def push(self, ele):
        self.__list.add_to_first(ele)
    
    def pop(self):
        return self.__list.remove_first()
    
    def peek(self):
        return self.__list.get_first()
    
    def __str__(self):
        string = 'Stack: top '
        string += str(self.__list)
        return string

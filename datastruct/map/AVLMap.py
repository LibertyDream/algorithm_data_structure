from Map import Map
from AVL import AVL

class AVLMap(Map):

    def __init__(self):
        self.__avl = AVL()
    
    def is_empty(self):
        return self.__avl.is_empty()
    
    def contains(self, key):
        return self.__avl.contains(key)

    def get_size(self):
        return self.__avl.get_size()

    def add(self, key, value):
        if self.__avl.get(key) is not None:
            self.__avl.set(key, value)
        else:
            self.__avl.add(key, value)
    
    def get(self, key):
        return self.__avl.get(key)

    def set(self, key, value):
        self.__avl.set(key, value)
    
    def remove(self, key):
        return self.__avl.remove(key)
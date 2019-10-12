from Set import Set
from AVL import AVL

class AVLSet(Set):

    def __init__(self):
        self.__avl = AVL()

    def is_empty(self):
        return self.__avl.is_empty()
    
    def get_size(self):
        return self.__avl.get_size()

    def add(self, ele):
        self.__avl.add(ele, None)
    
    def remove(self, ele):
        self.__avl.remove(ele)

    def contains(self, ele):
        return self.__avl.contains(ele)
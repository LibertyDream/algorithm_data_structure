from Map import Map

class Node(object):

    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.key) + ': ' + str(self.value)

class BSTMap(Map):

    def __init__(self):
        self.__size = 0
        self.__root = None
    
    def is_empty(self):
        return self.__size == 0
    
    def get_size(self):
        return self.__size

    def add(self, key, value):
        self.__root = self.__add(self.__root, key, value)

    
    def __add(self, node: Node, key, value):

        if node is None:
            self.__size += 1
            return Node(key, value)
        
        if key < node.key:
            node.left = self.__add(node.left, key, value)
        elif key > node.key:
            node.right = self.__add(node.right, key, value)
        else:
            node.value = value
        
        return node

    def get_node(self, key):
        if key is None:
            return None
        return self.__get_node(self.__root, key)
    
    def __get_node(self, node: Node, key):

        if node is None:
            return None

        if key < node.key:
            return self.__get_node(node.left, key)
        elif key > node.key:
            return self.__get_node(node.right, key)
        else:
            return node

    def contains(self, key):
        node = self.get_node(key)

        if node is None:
            return False
        else:
            return True
    
    def get(self, key):
        node = self.get_node(key)

        if node is None:
            return None
        else:
            return node.value

    def set(self, key, value):
        node = self.get_node(key)

        if node is None:
            raise IndexError('%s does not exist!' % key)

        node.value = value
    
    def __min(self, node: Node):

        if node is None:
            raise IndexError('Tree is empty!')

        if node.left is not None:
            return self.__min(node.left)
        
        return node

    def remove(self, key):
        ret = self.get_node(key)
        if ret is not None:
            ret = ret.value
            self.__root = self.__remove(self.__root, key)
        return ret

    def __remove(self, node: Node, key):

        if node is None:
            raise IndexError('Tree is empty!')

        if key < node.key:
            node.left = self.__remove(node.left, key)
        elif key > node.key:
            node.right = self.__remove(node.right, key)
        else: # key == node.key
            if node.left is None:
                self.__size -= 1
                ret = node.right
                node.right = None
                return ret
            elif node.right is None:
                self.__size -= 1
                ret = node.left
                node.left = None
                return ret
            else:
                ret = self.__min(node.right)
                ret.right = self.__remove(node.right, ret.key)
                ret.left = node.left
                node.right = node.left = None
                return ret

        return node

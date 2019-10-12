class Node(object):

    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.height = 1
    
    def __str__(self):
        return str(self.key) + ': ' + str(self.value)

class AVL(object):

    def __init__(self):
        self.__size = 0
        self.__root = None
    
    def is_empty(self):
        '''AVL树是否为空'''
        return self.__size == 0
    
    def get_size(self):
        '''AVL树的大小'''
        return self.__size

    def get_height(self, node: Node)-> int:
        '''获取结点高度'''
        if node is None:
            return 0
        return node.height

    def __get_balanced_factor(self, node: Node)-> int:
        '''获取结点平衡因子'''
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def __right_rotate(self, node: Node) -> Node:
        '''右旋转操作'''
        left = node.left
        left_max = left.right

        left.right = node
        node.left = left_max

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left.height = 1 + max(self.get_height(left.left), self.get_height(left.right))

        return left

    def __left_rotate(self, node: Node)-> Node:
        '''左旋转操作'''
        right = node.right
        right_min = right.left

        right.left = node
        node.right = right_min

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right.height = 1 + max(self.get_height(right.left), self.get_height(right.right))

        return right

    def add(self, key, value):
        self.__root = self.__add(self.__root, key, value)

    def __add(self, node: Node, key, value):
        '''向以node为根的AVL树中添加（key，value）键值对'''
        if node is None:
            self.__size += 1
            return Node(key, value)
        
        if key < node.key:
            node.left = self.__add(node.left, key, value)
        else:
            node.right = self.__add(node.right, key, value)

        # 更新高度
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance_factor = self.__get_balance_factor(node)

        if balance_factor > 1 and self.__get_balance_factor(node.left) >= 0:
            return self.right_rotate(node)
        if balance_factor < -1 and self.__get_balance_factor(node.right) <= 0:
            return self.left_rotate(node)
        if balance_factor > 1 and self.__get_balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance_factor < -1 and self.__get_balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)   

        return node

    def get_node(self, key):
        '''获取键值为 key 的结点'''
        if key is None:
            return None
        return self.__get_node(self.__root, key)
    
    def __get_node(self, node: Node, key):
        '''从以 node 为根的AVL树中寻找键值为 key 的结点并返回'''
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
        '''从以node为根的AVL树中删除键值为 key 的结点'''
        if node is None:
            raise IndexError('Tree is empty!')

        ret_node = None
        if key < node.key:
            node.left = self.__remove(node.left, key)
            ret_node = node
        elif key > node.key:
            node.right = self.__remove(node.right, key)
            ret_node = node
        else: # key == node.key
            if node.left is None:
                self.__size -= 1
                ret = node.right
                node.right = None
                ret_node = ret
            elif node.right is None:
                self.__size -= 1
                ret = node.left
                node.left = None
                ret_node = ret
            else:
                ret = self.__min(node.right)
                ret.right = self.__remove(node.right, ret.key)
                ret.left = node.left
                node.right = node.left = None
                ret_node = ret

        if ret_node is None:
            return None

        ret_node.height = 1 + max(self.get_height(ret_node.left), self.get_height(ret_node.right))

        balance_factor = self.__get_balance_factor(ret_node)

        if balance_factor > 1 and self.__get_balance_factor(ret_node.left) >= 0:
            ret_node = self.right_rotate(ret_node)
        if balance_factor < -1 and self.__get_balance_factor(ret_node.right) <= 0:
            ret_node = self.left_rotate(ret_node)
        if balance_factor > 1 and self.__get_balance_factor(ret_node.left) < 0:
            ret_node.left = self.left_rotate(ret_node.left)
            ret_node = self.right_rotate(ret_node)
        if balance_factor < -1 and self.__get_balance_factor(ret_node.right) > 0:
            ret_node.right = self.right_rotate(ret_node.right)
            ret_node = self.left_rotate(ret_node)           

        return ret_node

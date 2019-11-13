'''面试题37：序列化二叉树

请实现两个函数，分别用来序列化和反序列化二叉树。
'''
class Node(object):
    def __init__(self,value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST(object):

    def __init__(self):
        self.root = None
    
    def add(self, ele):
        if ele is None:
            return
        self.root = self.__add(self.root, ele)

    def __add(self, node: Node, ele):

        if node is None:
            return Node(ele)
        
        if ele > node.value:
            node.right = self.__add(node.right, ele)
        else:
            node.left = self.__add(node.left, ele)
        
        return node
    
    def pre_order(self):
        if self.root is None:
            return
        self.__pre_order(self.root)
    
    def __pre_order(self, node):
        if node is None:
            return

        print(node.value, end='')
        self.__pre_order(node.left)
        self.__pre_order(node.right)

def serialize(node):
    if node is None:
        return
    
    return ''.join(__serialize(node,[]))

def __serialize(node, ser_arr):

    if node is None:
        ser_arr.append('$')
        return ser_arr
    
    ser_arr.append(str(node.value))
    
    __serialize(node.left, ser_arr)
    __serialize(node.right, ser_arr)
    return ser_arr

def deserialize(ser_string):

    if ser_string is None or len(ser_string) == 0:
        return
    
    return __deserialize(ser_string, 0)[0]

def __deserialize(ser_string, index):

    if index >= len(ser_string) or ser_string[index] == '$':
        return None, index
    
    cur = Node(int(ser_string[index]))
    cur.left, index = __deserialize(ser_string, index + 1)
    cur.right, index = __deserialize(ser_string, index + 1)
    return cur, index

if __name__ == "__main__":

    bst = BST()
    datas = [5,3,1,7,6,8]
    for data in datas:
        bst.add(data)
    
    string = serialize(bst.root)
    print(string)
    bst.root = deserialize(string)
    bst.pre_order()
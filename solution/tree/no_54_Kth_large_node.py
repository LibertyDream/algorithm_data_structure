'''面试题54：二叉搜索树的第k大节点

给定一棵二叉搜索树，请找出其中第k大的节点。
-----------------
     5
  3      7
2   4   6  8

input: 3
output: 4
'''
class Node(object):
    def __init__(self, value, left=None, right=None):
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

    def in_order(self):
        if self.root is None:
            return
        self.__in_order(self.root)
    
    def __in_order(self, node):

        if node.left is not None:
            self.__in_order(node.left)
        
        print(node.value, end=' ')

        if node.right is not None:
            self.__in_order(node.right)

def Kth_node(root, k):

    if root is None or k <= 0:
        return None
    
    return __Kth_node(root, [k]).value

def __Kth_node(root, k):
    target =None

    if root.left is not None:
        target = __Kth_node(root.left, k)
    
    if target is None:
        if k[0] == 1:
            target = root
        k[0] -= 1
    
    if target is None and root.right is not None:
        target = __Kth_node(root.right, k)
    
    return target

if __name__ == "__main__":

    datas = [[[5,3,2,4,7,6,8],3]]

    for data in datas:
        arr, k = data
        bst = BST()
        for x in arr:
            bst.add(x)
        bst.in_order()
        print()
        print(k, Kth_node(bst.root, k))


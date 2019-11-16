'''面试题55-1：二叉树的深度

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）
形成树的一条路径，最长路径的长度为树的深度。
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


def get_deepth(node):
    if node is None:
        return 0

    left = get_deepth(node.left)
    right = get_deepth(node.right)

    return left + 1 if left > right else right + 1          

if __name__ == "__main__":

    data = [5,3,2,4,7,6,8]
    bst = BST()
    for x in data:
        bst.add(x)
    print(get_deepth(bst.root))
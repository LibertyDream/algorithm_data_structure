'''面试题55-2：平衡二叉树

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左、右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
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

def is_balanced(root):

    if root is None:
        return False
    
    return __is_balanced(root, [0])

def __is_balanced(root, depth):
    if root is None:
        depth[0] = 0
        return True
    l_depth = [0]
    r_depth = [0]
    if __is_balanced(root.left, l_depth) and __is_balanced(root.right, r_depth):
        dif = l_depth[0] - r_depth[0]
        if dif >= -1 and dif <= 1:
            depth[0] = l_depth[0] + 1 if l_depth[0] > r_depth[0] else r_depth[0] + 1
            return True
    return False

if __name__ == "__main__":

    datas = [[None], [5,3,2,4,7,6,8], [1,2,3],[1]]
    for data in datas:
        bst = BST()
        for i in data:
            bst.add(i)
        print(data, is_balanced(bst.root))
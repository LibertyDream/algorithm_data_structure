'''面试题28：对称的二叉树

请实现一个函数，用来判断一棵二又树是不是对称的。
如果一棵二叉树和它的镜像一样，那么它是对称的。
'''
class tree_node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_symmetric(root):

    if root is None:
        return False

    return __is_symmetric(root, root)

def __is_symmetric(root_1, root_2):

    if root_1 is None and root_2 is None:
        return True

    if root_1 is None or root_2 is None:
        return False

    if root_1.value != root_2.value:
        return False
    
    return __is_symmetric(root_1.left, root_2.right) and __is_symmetric(root_1.right, root_2.left)
'''面试题27：二叉树的镜像

请完成一个函数，输入一棵二叉树，该函数输出它的镜像
--------------
画图可以使问题变得直观
'''

class tree_node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_mirror_tree(root):

    if root is None:
        return None

    root.left, root.right = root.right, root.left

    if root.left is not None:
        root.left = get_mirror_tree(root.left)
    if root.right is not None:
        root.right = get_mirror_tree(root.right)
    return root
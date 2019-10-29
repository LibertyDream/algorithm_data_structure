'''面试题8：二又树的下一个节点

给定一棵二义树和其中的一个节点，找出中序遍历序列的下一个节点
树中的节点除了有两个分别指向左、右子节点的指针，还有一个指向父节点的指针。
'''

class Node(object):
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def find_next(node:Node):

    if node is None:
        return None

    ret = node.right

    if ret is not None:
        ret = ret.right
        while ret.left is not None:
            ret = ret.left
    elif node.parent is not None:
        parent = node.parent
        cur = node
        while parent is not None and parent.right == cur:
            cur = parent
            parent = cur.parent
        ret = parent

    return ret
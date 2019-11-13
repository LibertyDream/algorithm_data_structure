'''面试题32-1：从上到下打印二叉树

不分行从上到下打印二叉树,从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印
'''
from collections import deque

class Node(object):
    def __init__(self, value, left= None, right= None):
        self.value = value
        self.left = left
        self.right = right

def level_order(root:Node):

    if root is None:
        return
    
    dq = deque()
    dq.append(root)

    while len(dq) > 0:
        cur = dq.popleft()
        print(cur.value, end=' ')
        if cur.left is not None:
            dq.append(cur.left)
        if cur.right is not None:
            dq.append(cur.right)

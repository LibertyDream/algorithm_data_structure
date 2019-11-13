'''面试题32-2: 分行从上到下打印二叉树。

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
'''
from collections import deque

class Node(object):
    def __init__(self, value, left= None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_line_feed(root:Node):

    if root is None:
        return

    nums_next_level = 0
    nums_print = 1

    dq = deque()
    dq.append(root)
    while len(dq) > 0:
        cur = dq.popleft()

        print(cur, end=' ')

        if cur.left is not None:
            dq.append(cur.left)
            nums_next_level += 1
        if cur.right is not None:
            dq.append(cur.right)
            nums_next_level += 1
        
        nums_print -= 1
        if nums_print == 0:
            nums_print = nums_next_level
            print()
            nums_next_level = 0
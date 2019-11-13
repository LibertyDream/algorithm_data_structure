'''面试题32-3: 之字形打印二叉树

实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推
'''

class Node(object):
    def __init__(self, value, left= None, right= None):
        self.value = value
        self.left = left
        self.right = right

def z_print(root:Node):

    if root is None:
        return
    
    stacks = [[],[]]
    now = 0
    newline = 1

    stacks[now].append(root)
    while len(stacks[now]) > 0 or len(stacks[newline]) > 0:
        cur = stacks[now].pop()

        print(cur.value, end = ' ')

        if now == 0:

            if cur.left is not None:
                stacks[newline].append(cur.left)
            if cur.right is not None:
                stacks[newline].append(cur.right)
        else:
            if cur.right is not None:
                stacks[newline].append(cur.right)
            if cur.left is not None:
                stacks[newline].append(cur.left)
        
        if len(stacks[now]) == 0:
            now = 1-now
            newline = 1-newline
            print()
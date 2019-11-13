'''面试题34：二叉树中和为某一值的路径

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
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

def find_path(root:Node, expected_num:int):

    if root is None:
        return None

    path = []
    cur_sum = 0
    __find_path(root, expected_num, cur_sum, path)

def __find_path(node:Node, expected_num:int, cur_sum, path):

    cur_sum += node.value
    path.append(node)

    is_leaf = node.left is None and node.right is None

    if cur_sum == expected_num and is_leaf:
        for x in path:
            print(x.value, end=" ")
        print()
    
    if node.left is not None:
        __find_path(node.left, expected_num, cur_sum,path)
    if node.right is not None:
        __find_path(node.right, expected_num, cur_sum,path)

    path.pop()

if __name__ == "__main__":

    bst = BST()
    data = [10,5,12,4,7]
    for x in data:
        bst.add(x)

    find_path(bst.root, 22)
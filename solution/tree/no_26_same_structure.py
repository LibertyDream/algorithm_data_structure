'''面试题26：树的子结构

输入两棵二叉树A和B，判断B是不是A的子结构
------------
与二又树相关的代码有大量的指针操作，在每次使用指针的时候，
都要考虑这个指针有没有可能是空，如果是，该怎么处理。
'''

class tree_node(object):

    def __init__(self,value:float= 0.0,left_child=None,right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __eq__(self, other):
        return abs(self.value - other.value) < 1e-9

    def __lt__(self, other):
        return self.value - other.value < 0

def is_substruct(root_1:tree_node, root_2:tree_node):
    
    # 空集是任意集合的子集
    if root_2 is None:
        return True
    
    if root_1 is None:
        return False

    res = False

    if root_1 == root_2:
        res = __is_same(root_1, root_2)
    if not res:
        res = is_substruct(root_1.left_child, root_2)
    if not res:
        res = is_substruct(root_1.right_child, root_2)
    return res

def __is_same(root_1:tree_node, root_2:tree_node):

    # 比对完毕，结构一致
    if root_2 is None:
        return True

    if root_1 is None:
        return False
    
    if root_1 == root_2:
        return __is_same(root_1.left_child, root_2.left_child) and __is_same(root_1.right_child, root_2.right_child)
    
    return False
    
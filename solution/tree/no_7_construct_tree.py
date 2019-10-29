'''面试题7：重建二又树
题目：输入某二义树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
---------------
Example
input:前序遍历序列[1，2，4，7，3，5，6，8]和中序遍历序列[4，7，2，1，5，3，8，6]
output:根结点
    1
  2     3
4     5    6  
  7      8
'''
class Node(object):

    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def construct_tree(pre_arr, in_arr):

    if pre_arr is None or in_arr is None or len(pre_arr) == 0 or len(in_arr) == 0:
        return None

    return __construct_tree(pre_arr, in_arr, 0, len(pre_arr)-1, 0, len(in_arr)-1)

def __construct_tree(pre_arr, in_arr, pre_left, pre_right, in_left, in_right):

    if pre_left - pre_right != in_left - in_right:
        raise ValueError('input array is illegal')

    if pre_left > pre_right:
        return None
    
    root_value = pre_arr[pre_left]
    in_root_index = -1

    for i in range(in_left, in_right+1):
        if in_arr[i] == root_value:
            in_root_index = i
    
    if in_root_index == -1:
        raise ValueError('input array is illegal')

    root = Node(root_value)

    length = in_root_index - in_left

    root.left = __construct_tree(pre_arr, in_arr, pre_left + 1, pre_left + length, in_left, in_root_index - 1)
    root.right = __construct_tree(pre_arr, in_arr, pre_left + length + 1, pre_right, in_root_index + 1, in_right)

    return root

def __pre_order(root):

    if root == None:
        return
    
    print(root.value, end=' ')
    __pre_order(root.left)
    __pre_order(root.right)

def __in_order(root):

    if root == None:
        return
    
    __in_order(root.left)
    print(root.value, end=' ')
    __in_order(root.right)

if __name__ == "__main__":

    pre_arr = [1,2,4,7,3,5,6,8]
    in_arr = [4,7,2,1,5,3,8,6]
    
    # pre_arr = None
    # in_arr = None

    # pre_arr = []
    # in_arr = []

    # pre_arr = [1]
    # in_arr = [1]

    # pre_arr = [1,2]
    # in_arr = [1]

    root = construct_tree(pre_arr, in_arr)

    __pre_order(root)
    print()
    __in_order(root)
'''面试题33：二分搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。
-----------------
Example
input:[5,7,6,9,11,10,8]
output:True

input:[7,4,6,5]
output:False
'''

def is_post_order_BST(array):

    if array is None or len(array) == 0:
        return False
    
    return __is_post_order_BST(array, 0, len(array) - 1)

def __is_post_order_BST(array, start, end):

    if start >= end:
        return True
    
    root = array[end]

    lt = start
    while array[lt] < root:
        lt += 1
    
    gt = lt
    while gt < end:
        if array[gt] < root:
            return False
        gt += 1

    return __is_post_order_BST(array, start,lt-1) and __is_post_order_BST(array,lt,end-1)
    
    
if __name__ == "__main__":

    datas = [[5,7,6,9,11,10,8],[1,4,3,6,8,7,5],[7,4,6,5],[1,2,3,4],[4,3,2,1],[],None]
    for data in datas:
        print(data, is_post_order_BST(data))
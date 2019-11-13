'''面试题36：二叉搜索树与双向链表

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。
'''
class Node(object):
    def __init__(self, value=None, left=None, right=None):
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

def bst_to_linked_list(root:Node):

    if root is None:
        return None

    last_node = []
    __bst_to_linked_list(root, last_node)
    last_node = last_node[-1]

    while last_node is not None and last_node.left is not None:
        last_node = last_node.left
    
    return last_node

def __bst_to_linked_list(root, last_node):
    if root is None:
        return

    if root.left is not None:
        __bst_to_linked_list(root.left, last_node)

    root.left = None if len(last_node)== 0 else last_node[-1]
    if len(last_node) > 0:
        last_node[-1].right = root
    last_node.append(root)

    if root.right is not None:
        __bst_to_linked_list(root.right, last_node)


if __name__ == "__main__":

    datas = [[1,2,3,4,5],[5,4,3,2,1],[5,3,4,2,7,6,8]]

    for data in datas:
        bst = BST()
        for x in data:
            bst.add(x)
        head = bst_to_linked_list(bst.root)
        print(data, end="\t")
        while head is not None:
            print(head.value, end=" ")
            head = head.right
        print()
    
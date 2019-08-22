from BST import BST
from set import Set


class BSTSet(Set):

    def __init__(self):
        self.bst = BST()

    # 判断集合是否为空
    def is_empty(self):
        return self.bst.is_empty()

    # 添加 ele 至集合
    def add(self, ele):
        self.bst.add(ele)

    # 是否包含元素 ele
    def contains(self, ele):
        return self.bst.contains(ele)

    # 从集合内删除 ele
    def remove(self, ele):
        self.remove(ele)

    # 获取集合大小
    def get_size(self):
        return self.bst.get_size()
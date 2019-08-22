from LinkedList import LinkedList
from set import Set


class LinkedListSet(Set):

    def __init__(self):
        self.link_list = LinkedList()

    # 判断集合是否为空
    def is_empty(self):
        return self.link_list.is_empty()

    # 是否包含元素 ele
    def contains(self, ele):
        return self.link_list.contain(ele)

    # 如果未存储 ele，则加入集合
    def add(self, ele):
        if not self.contains(ele):
            self.link_list.add_to_first(ele)

    # 删除元素ele
    def remove(self, ele):
        self.link_list.remove_ele(ele)

    # 获取集合大小
    def get_size(self):
        self.link_list.get_size()

from Map import Map


class Node(object):
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LinkedListMap(Map):

    def __init__(self):
        self.__size = 0
        self.__dummy_head = Node()

    def is_empty(self):
        return self.__size == 0

    def get_size(self):
        return self.__size


    def __get_node(self, key):
        """辅助函数，寻找 key 所在的结点"""
        cur = self.__dummy_head.next

        while cur is not None:
            if cur.key == key:
                return cur

            cur = cur.next

        return None

    def contains(self, key):

        return self.__get_node(key) is not None

    def get(self, key):

        node = self.__get_node(key)

        if node is None:
            return None
        else:
            return node.value

    def add(self, key, value):

        node = self.__get_node(key)

        if node is None:
            self.__dummy_head.next = Node(key, value, self.__dummy_head.next)
            self.__size += 1
        else:
            node.value = value

    def set(self, key, value):

        node = self.__get_node(key)

        if node is None:
            raise IndexError("%s doesn't exist!" % key)
        else:
            node.value = value

    def remove(self, key):

        pre = self.__dummy_head

        while pre.next is not None:
            if pre.next.key == key:
                ret = pre.next
                pre.next = ret.next
                ret.next = None
                self.__size -= 1
                return ret.value

            pre = pre.next

        return None


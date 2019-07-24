class Node(object):
    def __init__(self, ele = None, next_node = None):
        self.data = ele
        self.next = next_node
    
    def __str__(self):
        return str(self.data)
    
class LinkedList(object):

    def __init__(self):
        self.__dummy_head = Node()
        self.__size = 0
    
    # 获取链表大小
    def get_size(self):
        return self.__size
    
    # 判断链表是否为空
    def is_empty(self):
        return self.__size == 0

    # 添加元素到指定位置
    # 方法不常用，仅做练习
    def add_to_index(self, index:int, ele):
        if index < 0 or index > self.__size:
            raise IndexError('Add failed! Index is illegal.')
        
        prev = self.__dummy_head
        for i in range(index):
            prev = prev.next
        prev.next = Node(ele, prev.next)
        self.__size += 1
    
    # 添加元素到末尾
    def add_to_last(self, ele):
        self.add_to_index(self.__size, ele)

    # 添加元素到头结点
    def add_to_first(self, ele):
        self.add_to_index(0, ele)
    
    # 删除指定位置的元素
    # 方法不常用，仅做练习
    def remove_by_index(self, index:int):
        if index < 0 or index >= self.__size:
            raise IndexError('Remove failed. Index is illegal')
        
        cur = self.__dummy_head
        for i in range(index):
            cur = cur.next
        
        ret = cur.next
        cur.next = ret.next
        ret.next = None

        self.__size -= 1

        return ret.data

    # 删除最后一个元素
    def remove_last(self):
        self.remove_by_index(self.__size - 1)

    # 删除第一个元素
    def remove_first(self):
        self.remove_by_index(0)

    # 将指定位置元素设定为给定值
    # 方法不常用，仅做练习
    def set(self, index:int, ele):
        if index < 0 or index >= self.__size:
            raise IndexError('Set failed! Index is illegal.')

        cur = self.__dummy_head.next
        for i in range(index):
            cur = cur.next
        
        cur.data = ele
    
    def get(self, index:int):
        if index < 0 or index >= self.__size:
            raise IndexError('Get failed! Index is illegal.')
        cur = self.__dummy_head.next
        for i in range(index):
            cur = cur.next
        return cur.data

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(self.__size - 1)
    
    # 判断是否包含指定元素
    def contain(self, ele):
        
        cur = self.__dummy_head
        while cur != None:
            if cur.data == ele:
                return True
            cur = cur.next
        return False
    
    def __str__(self):
        string = ''
        cur = self.__dummy_head.next
        while cur != None:
            string += str(cur) + '->'
            cur = cur.next
        string += 'null'
        return string
    

        
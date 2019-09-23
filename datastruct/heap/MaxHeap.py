from Array import Array

class MaxHeap(object):

    def __init__(self, arr=None):

        if arr is None:
            self.__data = Array()
        elif isinstance(arr, int):
            self.__data = Array(arr)
        else:
            # 如果 arr 不为空，使用 heapify 操作将 arr 整理成堆
            self.__data = Array(arr)
            i = (self.get_size() - 2) // 2
            while i >= 0:
                self.__sift_down(i)
                i -= 1


    # 堆大小
    def get_size(self):
        return self.__data.get_size()

    # 堆是否为空
    def is_empty(self):
        return self.__data.is_empty()

    # 起始索引为0的完全二叉树下，返回给定索引的父结点索引
    def get_parent(self, index: int):

        if index == 0:
            raise IndexError('index-0 has no parent')
        return (index - 1) // 2

    # 起始索引为0的完全二叉树下，返回给定索引的左孩子索引
    def get_left_child(self, index: int):
        return 2 * index + 1

    # 起始索引为0的完全二叉树下，返回给定索引的右孩子索引
    def get_right_child(self, index: int):
        return 2 * index + 2

    # 向堆内添加新元素 e
    def add(self, e):
        self.__data.add_to_last(e)
        self.__sift_up(self.__data.get_size() - 1)
    
    # 上浮操作
    def __sift_up(self, index: int):

        while index > 0 and self.__data.get(self.get_parent(index)) < self.__data.get(index):
            self.__data.swap(index, self.get_parent(index))
            index = self.get_parent(index)

    # 获取堆内最大元素
    def get_max(self):
        if self.get_size() == 0:
            raise IndexError('heap is empty')
        return self.__data.get(0)

    # 获取并从堆内删除最大元素
    def extract_max(self):
        ret = self.get_max()

        self.__data.set(0, ret)
        self.__data.remove_last()
        self.__sift_down(0)

        return ret

    # 下沉操作
    def __sift_down(self, index: int):

        while self.get_left_child(index) < self.get_size():

            j = self.get_left_child(index)
            if j + 1 < self.get_size() and self.__data.get(j + 1) > self.__data.get(j):
                j += 1
            if self.__data.get(index) > self.__data.get(j):
                break
            else:
                self.__data.swap(index, j)
                index = j
    
    # 取出堆内元素最大值，并替换为新值
    def replace(self, ele):
        ret = self.get_max()
        self.__data.set(0, ele)
        self.__sift_down(0)
        return ret

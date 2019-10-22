import sort_helper as sh

class IndexMaxHeap(object):

    def __init__(self, arr:list = None, indexes:list = None):

        if arr is None:
            self.__data = [None]*10
            self.__indexes = [None]*10
            self.__reversed = [None]*10
            self.__size = 0

        else:
            self.__data = arr
            self.__indexes = indexes
            self.__size = len(self.__data)
            self.__reversed = [None] * len(self.__data)
            start = self.__get_parent(self.__size - 1)
            while start >= 0:
                self.__shift_down(start)
                start -= 1
    
    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    # index: 用户眼中的 data 索引 data[i],代表优先级等
    def add(self, index, ele):
        if self.__size == len(self.__data):
            self.__resize(2 * self.__size)
        
        self.__data[index] = ele
        self.__indexes[self.__size] = index
        self.__reversed[index] = self.__size
        self.__shift_up(self.__size)
        self.__size += 1

    def peek(self):
        if self.__size == 0:
            return None
        return self.__data[self.__indexes[0]]
    
    def pop(self):
        if self.__size == 0:
            return None

        ret = self.__data[self.__indexes[0]]
        self.__indexes[0], self.__indexes[self.__size - 1] = self.__indexes[self.__size - 1], self.__indexes[0]
        self.__reversed[self.__indexes[self.__size - 1]] = None
        self.__reversed[self.__indexes[0]] = 0
        self.__size -= 1
        self.__shift_down(0)        

        if self.__size < len(self.__data) // 4:
            self.__resize(len(self.__data) // 2)

        return ret     
        
    def __get_parent(self, index):
        if index == 0:
            raise ValueError("0-index does not have a parent")
        return (index - 1) // 2
    
    def __get_left_child(self, index):
        return 2 * index + 1

    def __get_right_child(self, index):
        return 2 * index + 2

    def __shift_up(self, index):

        while index > 0 and self.__data[self.__indexes[index]] > self.__data[self.__indexes[self.__get_parent(index)]]:
            self.__indexes[index], self.__indexes[self.__get_parent(index)] = self.__indexes[self.__get_parent(index)], self.__indexes[index]
            self.__reversed[self.__indexes[index]] = index
            self.__reversed[self.__indexes[self.__get_parent(index)]] = self.__get_parent(index)
            index = self.__get_parent(index)            
    
    def __shift_down(self, index):

        while self.__get_left_child(index) < self.__size:

            swap = self.__get_left_child(index)
            if swap + 1 < self.__size and self.__data[self.__indexes[swap+1]] > self.__data[self.__indexes[swap]]:
                swap += 1
            
            if self.__data[self.__indexes[index]] > self.__data[self.__indexes[swap]]:
                break
            
            self.__indexes[index], self.__indexes[swap] = self.__indexes[swap], self.__indexes[index]
            self.__reversed[self.__indexes[swap]] = swap
            self.__reversed[self.__indexes[index]] = index
            index = swap
            
    def __resize(self, new_size):

        new_data = [None] * new_size
        new_indexes = [None] * new_size
        new_reversed = [None] * new_size
        for i in range(self.__size):
            new_data[i] = self.__data[i]
            new_indexes[i] = self.__indexes[i]
            new_reversed[i] = self.__reversed[i]
        self.__data = new_data
        self.__indexes = new_indexes
        self.__reversed = new_reversed

    def pop_index(self):

        if self.__size == 0:
            return -1

        ret = self.__indexes[0]

        self.__indexes[0], self.__indexes[self.__size - 1] = self.__indexes[self.__size - 1], self.__indexes[0]
        self.__reversed[self.__indexes[self.__size - 1]] = None
        self.__reversed[self.__indexes[0]] = 0
        self.__size -= 1
        self.__shift_down(0)

        if self.__size < len(self.__data) // 4:
            self.__resize(len(self.__data) // 2)
        
        return ret

    def get(self, index):
        return self.__data[index]

    def change(self, index, value):

        self.__data[index] = value

        loc = self.__reversed[index]

        self.__shift_down(loc)
        self.__shift_up(loc)
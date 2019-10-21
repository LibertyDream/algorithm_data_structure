class MaxHeap(object):

    def __init__(self, arr:list = None):

        if arr is None:
            self.__data = [None]*10
            self.__size = 0

        else:
            self.__data = arr
            self.__size = len(self.__data)
            start = self.__get_parent(self.__size - 1)
            while start >= 0:
                self.__shift_down(start)
                start -= 1
    
    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def add(self, ele):
        if self.__size == len(self.__data):
            self.__resize(2 * self.__size)
        
        self.__data[self.__size] = ele
        self.__shift_up(self.__size)
        self.__size += 1

    def peek(self):
        if self.__size == 0:
            return None
        return self.__data[0]
    
    def remove(self):
        if self.__size == 0:
            return None

        ret = self.__data[0]
        self.__data[0] = self.__data[self.__size - 1]
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

        while index > 0 and self.__data[index] > self.__data[self.__get_parent(index)]:
            self.__data[index], self.__data[self.__get_parent(index)] = self.__data[self.__get_parent(index)], self.__data[index]
            index = self.__get_parent(index)

            
    
    def __shift_down(self, index):

        while self.__get_left_child(index) < self.__size:

            swap = self.__get_left_child(index)
            if swap + 1 < self.__size and self.__data[swap + 1] > self.__data[swap]:
                swap += 1
            
            if self.__data[index] > self.__data[swap]:
                break
            
            self.__data[index], self.__data[swap] = self.__data[swap], self.__data[index]
            index = swap
            
    def __resize(self, new_size):

        new_data = [None] * new_size

        for i in range(self.__size):
            new_data[i] = self.__data[i]
        
        self.__data = new_data
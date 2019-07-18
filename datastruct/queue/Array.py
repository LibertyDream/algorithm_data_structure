class Array(object):

    #  通过条件语句实现重载
    def __init__(self, *a_array:int):

        #  Array（capacity）
        if len(a_array) == 1:
            self.__data = [None]*a_array[0]
            self.__size = 0

        #  Array()
        elif len(a_array) == 0:
            self.__data = [None] * 10
            self.__size = 0

        #  Array(1,2,3...)
        else:
            self.__data = [None] * 2 * len(a_array)
            for x in range(len(a_array)):
                self.__data[x] = a_array[x]
            self.__size = len(a_array)

    #  获取数组容量
    def get_capacity(self):
        return len(self.__data)

    #  获取数组大小
    def get_size(self):
        return self.__size


    #  设置数组打印格式
    def __str__(self):
        build_str = 'Array size: %d, capacity：%d\n' % (self.__size, len(self.__data))
        build_str += '['
        for i in range(self.__size):

            build_str = build_str + str(self.__data[i])
            if i < self.__size - 1:
                build_str += ', '
        build_str += ']'
        return build_str


    #  添加元素到末尾
    def add_to_last(self, ele):
        self.add_to_index(self.__size, ele)


    #  添加元素到头部
    def add_to_first(self, ele):
        self.add_to_index(0, ele)


    #  添加元素到给定索引处
    def add_to_index(self, index:int, ele):

        if index < 0 or index > self.__size:
            raise IndexError('Add failed. Index should between 0 and size')

        if self.__size == len(self.__data):
            self.__resize(2 * len(self.__data))

        for i in range(self.__size, index, -1):
            self.__data[i] = self.__data[i - 1]


        self.__data[index] = ele
        self.__size += 1

    #  数组扩容
    def __resize(self, new_capacity:int):
        new_data = [None] * new_capacity
        for i in range(self.__size):
            new_data[i] = self.__data[i]
        self.__data = new_data

    #  将给定索引处的值设为指定值
    def set(self, index:int, ele):

        if index < 0 or index > self.__size:
            raise IndexError('Set failed. Index should between 0 and size')
        self.__data[index] = ele


    #  返回给定索引处的值
    def get(self, index:int):

        if index < 0 or index > self.__size:
            raise IndexError('Get failed. Index should between 0 and size')
        return self.__data[index]

    #  返回末尾元素
    def get_last(self):
        return self.get(self.__size - 1)

    #  返回首位元素
    def get_first(self):
        return self.get(0)

    #  判断是否数组为空
    def is_empty(self):
        return self.__size == 0

    #  判断是否存在给定元素
    def contain(self, ele):
        for i in range(self.__size):
            if self.__data[i] == ele:
                return True
        return False

    #  返回第一处与ele相等的元素位置索引，否则返回-1
    def find(self, ele):
        for i in range(self.__size):
            if self.__data[i] == ele:
                return i
        return -1

    #  返回所有与ele相等的元素位置索引，否则返回none
    def find_all(self, ele):
        res = []
        for i in range(self.__size):
            if self.__data[i] == ele:
                res.append(i)
        if len(res) == 0:
            return None
        return res

    #  删除指定位置元素
    def remove_by_index(self, index:int):

        if index < 0 or index > self.__size:
            raise IndexError('Remove failed. Index should between 0 and size')

        for i in range(index, self.__size - 1):
            self.__data[i] = self.__data[i + 1]

        self.__size -= 1

        if self.__size < len(self.__data) / 4:
            self.__resize(len(self.__data) // 2)

    #  删除头元素
    def remove_first(self):
        self.remove_by_index(0)

    #  删除末尾元素
    def remove_last(self):
        self.remove_by_index(self.__size-1)

    #  删除第一个和给定值相等的元素
    def remove_ele(self, ele):

        index = self.find(ele)
        self.remove_by_index(index)

    #  删除所有和给定值相等的元素
    def remove_all_ele(self, ele):

        lt = self.find_all(ele)
        lt = lt[::-1]  #  索引倒序删除
        for index in lt:
            self.remove_by_index(index)

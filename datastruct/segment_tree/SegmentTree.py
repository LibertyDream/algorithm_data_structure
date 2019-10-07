class SegmentTree(object):

    def __init__(self, data:list, merger):
        '''
            初始化线段树
        __data：
            区间内的数据
        __tree:
            构建的线段树
        __merger:
            自定义的融合规则，通常是 lambda 表达式传来的 function 对象
        '''
        self.__merger = merger
        self.__data = data
        self.__tree = [None] * len(data) * 4
        self.__build_tree(0,0,len(self.__data) - 1)


    def __build_tree(self, tree_index:int, left, right):

        if left == right:
            self.__tree[tree_index] =  self.__data[left]
            return
        
        mid = left + (right - left) // 2
        left_index = self.left_child(tree_index)
        right_index = self.right_child(tree_index)
        self.__build_tree(left_index, left, mid)
        self.__build_tree(right_index, mid + 1, right)

        self.__tree[tree_index] = self.__merger(self.__tree[left_index], self.__tree[right_index])

    def get_size(self):
        return len(self.__data)

    def is_empty(self):
        return len(self.__data) == 0

    def left_child(self, index:int):
        return 2 * index + 1

    def right_child(self, index:int):
        return 2 * index + 2

    def query(self, queryL: int, queryR: int):
        '''
            查询 [queryL...queryR] 范围内的内容
        '''
        if (queryL < 0 or queryL >= len(self.__data) 
        or queryR < 0 or queryR >= len(self.__data)):
            raise IndexError("Index is illegal")

        return self.__query(0, 0, len(self.__data) - 1, queryL, queryR)
    
    def __query(self, tree_index:int, left, right, queryL:int, queryR:int):
        '''
            查询以 treeIndex 为根，[left,right] 为界，目标范围为 [queryL,queryR] 中的内容
        '''
        if left == queryL and right == queryR:
            return self.__tree[tree_index]
        
        mid = left + (right - left) // 2
        left_index = self.left_child(tree_index)
        right_index = self.right_child(tree_index)

        if queryL > mid:
            return self.__query(right_index, mid+1, right, queryL, queryR)
        elif queryR <= mid:
            return self.__query(left_index, left, mid, queryL, queryR)

        left_res = self.__query(left_index, left, mid, queryL, mid)
        right_res = self.__query(right_index, mid+1, right, mid + 1, queryR)
        return self.__merger(left_res, right_res)

    def update(self, index:int, ele):
        '''
            更新 index 处的值为 ele
        '''
        if index < 0 or index >= len(self.__data):
            raise IndexError("Invalid index")

        self.__data[index] = ele
        self.__update(0, 0, len(self.__data) - 1, index, ele)

    def __update(self, tree_index: int, left: int, right: int, index:int, ele):
        '''
            在以 treeIndex 为根的 [left,right] 的区间内更新 index 处的值为 e
        '''
        if left == right:
            self.__tree[tree_index] = ele
            return
        
        mid = left + (right - left) // 2
        left_index = self.left_child(tree_index)
        right_index = self.right_child(tree_index)

        if index > mid:
            self.__update(right_index, mid+1, right, index, ele)
        else:
            self.__update(left_index, left, mid, index, ele)
        
        self.__tree[tree_index] = self.__merger(self.__tree[left_index], self.__tree[right_index])

    def __str__(self):
        string = "["
        for i in range(len(self.__tree)):
            if self.__tree[i] is not None:
                string += str(self.__tree[i])
            else:
                string += "null"
            
            if i < len(self.__tree) - 1:
                string += ", "
        string += "]"
        return string
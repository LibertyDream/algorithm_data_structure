from UF import UF

class UnionFind(UF):

    def __init__(self, size:int) -> None:
        self.parent = [None] * size
        self.rank = [None] * size
        for i in range(size):
            self.parent[i] = i
            self.rank[i] = 1
    
    def get_size(self) -> int:
        return len(self.parent)
   
    # 找到 index 所在集合的根结点
    def __find(self, index:int) ->int:

        if index < 0 or index >= len(self.parent):
            raise IndexError("Index out of range")

        while index != self.parent[index]:
            self.parent[index] = self.parent[self.parent[index]]
            index = self.parent[index]

        # 第二种路径压缩，通过递归实现将路径高度压缩至2
        # if index != self.parent[index]:
        #     self.parent[index] = self.__find(self.parent[index])
        #     index = self.parent[index]
        return index
    
    # 判断 p，q 是否在一个集合内
    def is_connected(self, p:int, q:int) -> bool:
        return self.parent[p] == self.parent[q]

    # 合并 p，q 所在集合
    def union(self, p:int, q:int) -> None:

        p_root = self.__find(p)
        q_root = self.__find(q)

        if q_root == p_root:
            return
        
        if self.rank[p] < self.rank[q]:
            self.parent[p] = q_root
        elif self.rank[p] > self.rank[q]:
            self.parent[q] = p_root
        else:
            self.parent[q] = p_root
            self.rank[p_root] += 1
from min_heap import MinHeap
from weighted_dense_graph import WeightedDenseGraph as wdg
from weighted_sparse_graph import WeightedSparseGraph as wsg

class LazyPrim(object):
    '''使用懒惰 Prim 算法获取最小生成树 O(ElogE) E:edge_num'''
    def __init__(self, graph, heap):

        self.__graph = graph
        self.__visited = [False] * graph.get_node_nums()
        self.__heap = heap
        self.__weight = 0
        self.__tree = []
        self.__visit(0)
        

        while not self.__heap.is_empty():
            edge = self.__heap.pop()            
            if self.__visited[edge.orgin] == self.__visited[edge.goal]:
                continue
            self.__tree.append(edge)
            if self.__visited[edge.orgin]:
                self.__visit(edge.goal)
            else:
                self.__visit(edge.orgin)   

        for x in self.__tree:
            self.__weight += x.weight        

    def __visit(self, node):

        self.__visited[node] = True
        adj = self.__graph.iter_nodes(node)
        for item in adj:
            if not self.__visited[item.other(node)]:
                self.__heap.add(item)
    
    def get_graph_weight(self):
        return self.__weight

    def get_tree(self):
        return self.__tree

datas = [[8,16],
        [4,5,.35],
        [4,7,.37],
        [5,7,.28],
        [0,7,.16],
        [1,5,.32],
        [0,4,.38],
        [2,3,.17],
        [1,7,.19],
        [0,2,.26],
        [1,2,.36],
        [1,3,.29],
        [2,7,.34],
        [6,2,.40],
        [3,6,.52],
        [6,0,.58],
        [6,4,.93]]

def init(graph, data):
    nums_node, nums_edge = data[0]
    ret = graph(nums_node)
    for i in range(1,len(data)):
        orgin, goal, weight = data[i]
        ret.add_edge(orgin, goal, weight)
    
    return ret

if __name__ == "__main__":

    graph = init(wsg, datas)
    lp = LazyPrim(graph, MinHeap())
    print(lp.get_graph_weight())


from weighted_sparse_graph import WeightedSparseGraph as wsg
from UnionFind import UnionFind
from min_heap import MinHeap

class Kruskal(object):
    '''借助并查集实现 Kruskal 算法求最小生成树 O(ElogE)'''

    def __init__(self, graph):

        self.__tree = []
        self.__weight = 0

        heap = MinHeap()
        for i in range(graph.get_node_nums()):
            adj = graph.iter_nodes(i)
            for edge in adj:
                if edge.orgin < edge.goal:
                    heap.add(edge)
        
        union_find = UnionFind(graph.get_node_nums())
        while not heap.is_empty() and len(self.__tree) < graph.get_node_nums() - 1:

            edge = heap.pop()
            
            if not union_find.is_connected(edge.orgin,edge.goal):
                self.__tree.append(edge)
                union_find.union(edge.orgin,edge.goal)

        for x in self.__tree:
            self.__weight += x.weight

    def get_graph_weight(self):
        return self.__weight

    def get_min_span_tree(self):
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
    kr = Kruskal(graph)
    for x in kr.get_min_span_tree():
        print('%d-%d: %.2f' % (x.orgin, x.goal, x.weight))
    print(kr.get_graph_weight())    

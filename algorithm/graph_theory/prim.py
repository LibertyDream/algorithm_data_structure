from index_min_heap import IndexMinHeap
from weighted_dense_graph import WeightedDenseGraph as wdg
from weighted_sparse_graph import WeightedSparseGraph as wsg

class Prim(object):
    '''借助最小索引堆实现的 Prim 算法，获取最小生成树 O(ElogV)'''

    def __init__(self, graph, heap):

        self.__graph = graph
        self.__heap = heap
        self.__visited = [False] * graph.get_node_nums()
        self.__edge_to = [None] * graph.get_node_nums()
        self.__weight = 0
        self.__tree = []

        # Prim

        self.__visit(0)

        while not self.__heap.is_empty():

            node = self.__heap.pop_index()
            self.__tree.append(self.__edge_to[node])
            self.__visit(node)
        
        for x in self.__tree:
            self.__weight += x.weight



    def __visit(self, node):

        self.__visited[node] = True
        adj = self.__graph.iter_nodes(node)
        for item in adj:
            goal = item.other(node)
            if not self.__visited[goal]:
                if self.__edge_to[goal] is None:
                    self.__edge_to[goal] = item
                    self.__heap.add(goal, item.weight)
                elif self.__edge_to[goal].weight > item.weight:
                    self.__edge_to[goal] = item
                    self.__heap.change(goal, item.weight)
                
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
    lp = Prim(graph, IndexMinHeap(graph.get_node_nums()))
    for x in lp.get_min_span_tree():
        print('%d-%d: %.2f' % (x.orgin, x.goal, x.weight))
    print(lp.get_graph_weight())    
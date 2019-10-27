from weighted_sparse_graph import WeightedSparseGraph as wsg
from index_min_heap import IndexMinHeap

class Dijkstra(object):
    '''借助最小索引堆实现有向带权图的单源最短路径算法 O(ElogV)
        Dijkstra 算法要求没有负权边
    '''

    def __init__(self, graph, orgin):
        self.__graph = graph
        self.__orgin = orgin
        self.__visited = [False] * graph.get_node_nums()
        self.__weight_to = [0] * graph.get_node_nums()
        self.__from = [-1] * graph.get_node_nums()

        imh = IndexMinHeap(graph.get_edge_nums())

        # Dijkstra
        imh.add(orgin, 0)
        while not imh.is_empty():

            node = imh.pop_index()
            self.__visited[node] = True

            # 松弛操作 relaxation
            edges = self.__graph.iter_nodes(node)
            for edge in edges:
                goal = edge.other(node)                
                if not self.__visited[goal]:
                    if self.__from[goal] == -1 or self.__weight_to[node] + edge.weight < self.__weight_to[goal]:
                        self.__weight_to[goal] = self.__weight_to[node] + edge.weight
                        self.__from[goal] = node
                        if imh.get(goal) is None:
                            imh.add(goal, self.__weight_to[goal])
                        else:
                            imh.change(goal, self.__weight_to[goal])

    def has_path(self, node):
        return self.__visited[node]

    def get_path(self, node):
        ret = []

        if not self.has_path(node):
            return ret

        while node != -1:
            ret.append(node)
            node = self.__from[node]
        
        return ret[::-1]
    
    def show_path(self, node):

        path = self.get_path(node)

        string = ''
        for item in path:

            string += '%d ' % item
            if item != node:
                string += '-> '
        
        print(string)

    def path_weight_to(self, node):
        
        if not self.has_path(node):
            return -1

        return self.__weight_to[node]
            

datas = [[5, 8],
        [0,1,5],
        [0,2,2],
        [0,3,6],
        [2,1,1],
        [2,3,3],
        [2,4,5],
        [1,4,1],
        [3,4,2]]
        
def init(graph, data, directed = False):
    node_nums, edge_nums = data[0]
    ret = graph(node_nums, directed)
    for i in range(1, edge_nums):
        orgin, goal, weight = data[i]
        ret.add_edge(orgin, goal, weight)
    return ret

if __name__ == "__main__":

    graph = init(wsg, datas, False)
    dj = Dijkstra(graph, 0)
    for i in range(1,graph.get_node_nums()):
        print('show path to %d, path weight:%.2f' % (i, dj.path_weight_to(i)))
        dj.show_path(i)
from weighted_sparse_graph import WeightedSparseGraph as wsg

class Bellman(object):
    '''在带有负权边的图中寻找单源最短路径 O(EV)

    思想：
        1.松弛操作的本质是查看对当前结点，如果多加一条边整个路径权值会不会更小
        2.如果一个图中有 V 个结点，当不存在负权环时，到达任意一点的路径长度最大为 V-1
        3.因此对所有结点执行 V-1 次松弛操作即可得到单源最短路径
        4.如果执行第 V 次松弛操作仍然有效，说明存在负权环
    '''

    def __init__(self, graph, orgin):
        self.__graph = graph
        self.__orgin = orgin
        self.__from = [None] * graph.get_node_nums()
        self.__weight_to = [0] * graph.get_node_nums()
        self.__has_cycle = False
        
        # Bellman-Ford
        for i in range(1, graph.get_node_nums()):
            for node in range(graph.get_node_nums()):
                edges = graph.iter_nodes(node)
                for edge in edges:
                    goal = edge.other(node)
                    if self.__from[goal] is None or self.__weight_to[goal] > self.__weight_to[node] + edge.weight:
                        self.__from[goal] = node
                        self.__weight_to[goal] = self.__weight_to[node] + edge.weight
        self.__has_cycle = self.__detect()

    def __detect(self):
        for node in range(graph.get_node_nums()):
            edges = graph.iter_nodes(node)
            for edge in edges:
                goal = edge.other(node)
                if self.__from[goal] is None or self.__weight_to[goal] > self.__weight_to[node] + edge.weight:
                    return True
        return False

    def has_path(self, node):

        return self.__from[node] is not None

    def get_path(self, node):
        
        ret = []

        if self.has_cycle():
            print('There is a negative right cycle')
            return ret
        if not self.has_path(node):
            return ret

        while node is not None:
            ret.append(node)
            node = self.__from[node]
        return ret[::-1]

    def has_cycle(self):
        return self.__has_cycle

    def path_weight_to(self, node):

        if self.has_cycle():
            print('There is a negative right circle')
            return float('inf')
        
        if not self.has_path(node):
            return float('inf')
        
        return self.__weight_to[node]

    def show_path(self, node):

        path = self.get_path(node)

        string = ''

        for item in path:
            
            string += '%d ' % item
            if item != node:
                string += '-> '
        
        print(string)

datas = [[5, 8],
        [0,1,5],
        [0,2,2],
        [0,3,6],
        [1,2,-4],
        [2,3,3],
        [2,4,5],
        [1,4,2],
        [4,3,-3]]
        
def init(graph, data, directed = False):
    node_nums, edge_nums = data[0]
    ret = graph(node_nums, directed)
    for i in range(edge_nums):
        orgin, goal, weight = data[1+i]
        ret.add_edge(orgin, goal, weight)
    return ret

if __name__ == "__main__":

    graph = init(wsg, datas, True)
    bf = Bellman(graph, 0)
    if bf.has_cycle():
        print('There is a negative right circle')
    else:
        for i in range(1,graph.get_node_nums()):
            print('show path to %d, path weight:%.2f' % (i, bf.path_weight_to(i)))
            bf.show_path(i)
    
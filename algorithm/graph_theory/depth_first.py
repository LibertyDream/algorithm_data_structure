import dense_graph as dg
import sparse_graph as sg

data = [[13,13],
        [0,5],
        [4,3],
        [0,1],
        [9,12],
        [6,4],
        [5,4],
        [0,2],
        [11,12],
        [9,10],
        [0,6],
        [7,8],
        [9,11],
        [5,3]]

class Component(object):
    '''
        深度优先遍历，获取连通分量
    '''
    def __init__(self, graph):
        self.__graph = graph
        self.__ccount = 0
        self.__id = [-1] * self.__graph.get_node_nums()
        self.__visited = [False] * self.__graph.get_node_nums()
  
        for i in range(self.__graph.get_node_nums()):
            if not self.__visited[i]:
                self.__dfs(i)
                self.__ccount += 1
        
    
    def __dfs(self, node):

        self.__visited[node] = True
        self.__id[node] = self.__ccount

        adj = self.__graph.iter_nodes(node)
        for node in adj:
            if not self.__visited[node]:
                self.__dfs(node)
            

    def is_connected(self, a, b):
        return self.__id[a] == self.__id[b]

    def count(self):
        return self.__ccount


def init(graph, data):
    nums_node, nums_edge = data[0]
    ret = graph(nums_node)
    for i in range(nums_edge):
        orign, goal = data[1 + i]
        ret.add_edge(orign, goal)
    return ret

if __name__ == "__main__":

    sparse = init(sg.SparseGraph, data)
    dense = init(dg.DenseGraph, data)

    cp = Component(sparse)
    print(cp.count())
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

class Path(object):

    def __init__(self, graph, orgin):

        self.__graph = graph
        self.__orgin = orgin
        self.__visited = [False] * graph.get_node_nums()
        self.__from = [-1] * graph.get_node_nums()

        # 以 orgin 为起点构建连通路径
        self.__dfs(orgin)

    def __dfs(self, node):
        self.__visited[node] = True
        adj = self.__graph.iter_nodes(node)
        for item in adj:
            if not self.__visited[item]:
                self.__from[item] = node
                self.__dfs(item)

    def has_path(self, node):

        if node < 0 or node >= self.__graph.get_node_nums():
            raise IndexError('node index out of range')

        return self.__visited[node]
    
    def get_path(self, node):
        '''返回 orgin 到 node 的路径'''
        ret = []
        if not self.has_path(node):
            return ret
        p = node
        while p != -1:
            ret.append(p)
            p = self.__from[p]
        
        return ret[::-1]

    def show_path(self, node):
        '''展示 orgin 到 node 的路径'''

        ret = ''
        if not self.has_path(node):
            return ret
        
        path = self.get_path(node)
        for x in path:
            ret += '%d ' % x
            if x != node:
                ret += '-> '
        
        print(ret)

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

    path = Path(sparse, 0)
    print(sparse)
    print()
    path.show_path(4)
    
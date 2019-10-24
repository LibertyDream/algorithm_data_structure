from collections import deque
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

class ShortestPath(object):
    '''广度优先遍历求解最短路径'''

    def __init__(self, graph, orgin):
        self.__graph = graph
        self.__orgin = orgin
        self.__visited = [False] * graph.get_node_nums()
        self.__from = [-1] * graph.get_node_nums()
        self.__ord = [-1] * graph.get_node_nums()

        dq = deque()
        dq.append(self.__orgin)
        self.__visited[self.__orgin] = True
        self.__ord[self.__orgin] = 0
        while len(dq) > 0:

            cur = dq.popleft()
            adj = graph.iter_nodes(cur)
            for node in adj:
                if not self.__visited[node]:
                    dq.append(node)
                    self.__visited[node] = True
                    self.__ord[node] = self.__ord[cur] + 1
                    self.__from[node] = cur
            
    def has_path(self, node):

        if node < 0 or node >= self.__graph.get_node_nums():
            raise ValueError('index out of range')

        return self.__visited[node]


    def path(self, node):

        if not self.has_path(node):
            return []

        ret = []
        cur = node

        while cur != -1:

            ret.append(cur)
            cur = self.__from[cur]

        return ret[::-1]

    def show_path(self,node):

        if not self.has_path(node):
            print('No path to node')

        path = self.path(node)

        string = ''

        for x in path:

            string += '%d ' % x

            if x != node:
                string += '-> '
        
        print(string)

    def path_length(self,node):

        if not self.has_path(node):
            return -1

        return self.__ord[node]

        
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

    path = ShortestPath(sparse, 0)
    print(sparse)
    print()
    path.show_path(3)
    # x = [1,2,3,4,5]
    # dq =deque()
    # for i in x:
    #     dq.append(i)
    # print(dq)
    # for i in range(len(x)):
    #     print(dq.popleft(),end =' ')

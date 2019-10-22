class DenseGraph(object):

    def __init__(self, nums_node, directed = False):

        self.__nums_node = nums_node
        self.__edges =[]
        self.__nums_edges = 0
        self.__directed = directed
        for i in range(nums_node):
            self.__edges.append([False]*nums_node)

    def has_edge(self, orgin, goal):

        if orgin < 0 or orgin >= self.__nums_node or goal < 0 or goal >= self.__nums_node:
            raise IndexError("Invalid node index")

        return self.__edges[orgin][goal]
    
    def add_edge(self, orgin, goal):

        if orgin < 0 or orgin >= self.__nums_node or goal < 0 or goal >= self.__nums_node:
            raise IndexError("Invalid node index")

        if not self.has_edge(orgin, goal):

            self.__edges[orgin][goal] = True

            if not self.__directed:
                self.__edges[goal][orgin] = True

            self.__nums_edges += 1
    
    def get_node_nums(self):
        return self.__nums_node

    def get_edge_nums(self):
        return self.__nums_edges

    def iter_nodes(self, node):
        ret = []
        for i in range(self.__nums_node):
            if self.__edges[node][i]:
                ret.append(i)
        return iter(ret)
    
    def __str__(self):
        ret = ''
        for i in range(self.__nums_node):
            for j in range(self.__nums_node):
                ret += '%d ' % self.__edges[i][j]
            ret += '\n'
        return ret
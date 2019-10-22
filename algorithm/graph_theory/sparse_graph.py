class SparseGraph(object):

    def __init__(self, nums_node, directed = False):
        self.__nums_node = nums_node
        self.__edges = []
        self.__nums_edges = 0
        self.__directed = directed
        for i in range(nums_node):
            self.__edges.append([])

    def add_edge(self, orgin, goal):

        if orgin < 0 or orgin >= self.__nums_node or goal < 0 or goal >= self.__nums_node:
            raise IndexError("Invalid node index")
        
        if not self.has_edge(orgin, goal):
            self.__edges[orgin].append(goal)

            if not self.__directed and orgin != goal:
                self.__edges[goal].append(orgin)
            
            self.__nums_edges += 1
    
    def has_edge(self, orgin, goal):

        if orgin < 0 or orgin >= self.__nums_node or goal < 0 or goal >= self.__nums_node:
            raise IndexError("Invalid node index")

        for node in self.__edges[orgin]:
            if node == goal: 
                return True
        
        return False

    def get_node_nums(self):
        return self.__nums_node

    def get_edge_nums(self):
        return self.__nums_edges

    def iter_nodes(self, node):
        return iter(self.__edges[node])

    def __str__(self):
        ret = ''
        for i in range(self.__nums_node):
            ret += '%d: ' % i
            for j in range(len(self.__edges[i])):
                ret += '%d ' % self.__edges[i][j]
            ret += '\n'
        return ret

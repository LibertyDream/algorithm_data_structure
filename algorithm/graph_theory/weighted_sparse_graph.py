class Edge(object):

    def __init__(self, orgin, goal, weight):

        self.orgin = orgin
        self.goal = goal
        self.weight = weight

    def other(self, orgin):

        if not (orgin == self.orgin or orgin == self.goal):
            raise ValueError("{} is not a valid point".format(orgin))

        return self.orgin if orgin == self.goal else self.goal
    
    def __eq__(self, other):

        return self.weight == other.weight

    def __lt__(self, other):

        return self.weight < other.weight

    def __str__(self):

        return '{To: %d, weight: %s}' % (self.goal, str(self.weight))

class WeightedSparseGraph(object):

    def __init__(self, node_nums, directed = False):

        self.__nums_node = node_nums
        self.__nums_edges = 0
        self.__directed = directed
        self.__edges = []
        for i in range(node_nums):
            self.__edges.append([])

    def has_edge(self, orgin, goal):

        if orgin < 0 or orgin >= self.__nums_node or goal < 0 or goal >= self.__nums_node:
            raise IndexError('index out of range')

        for x in self.__edges[orgin]:
            if x.other(orgin) == goal:
                return True

        return False

    def add_edge(self, orgin, goal, weight):

        if orgin < 0 or orgin >= self.__nums_node or goal < 0 or goal >= self.__nums_node:
            raise IndexError('index out of range')

        if self.has_edge(orgin, goal):

            for i in range(len(self.__edges[orgin])):

                if self.__edges[orgin][i].other(orgin) == goal:
                    self.__edges[orgin][i] = Edge(orgin, goal, weight)

                    if not self.__directed:
                        for y in len(self.__edges[goal]):
                            if self.__edges[goal][y].other(goal) == orgin:
                                self.__edges[goal][y] = Edge(goal, orgin, weight)

        else:      

            self.__edges[orgin].append(Edge(orgin, goal, weight))
            self.__nums_edges += 1
            if not self.__directed:
                self.__edges[goal].append(Edge(goal, orgin, weight))

    def get_node_nums(self):
        return self.__nums_node

    def get_edges(self):
        return self.__edges

    def get_edge_nums(self):
        return self.__nums_edges

    def iter_nodes(self, node):
        return iter(self.__edges[node])

    def __str__(self):

        string =''

        for i in range(len(self.__edges)):
            string += '%d: ' % i
            for edge in self.__edges[i]:
                string += '%s ' % str(edge)
            string += '\n'
        
        return string

data = [[8,16],
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

if __name__ == "__main__":
    nums_node, nums_edge = data[0]
    wsg = WeightedSparseGraph(nums_node)
    for i in range(1,len(data)):
        orgin, goal, weight = data[i]
        wsg.add_edge(orgin, goal, weight)
    print(wsg)

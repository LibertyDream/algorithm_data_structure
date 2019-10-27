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

class WeightedDenseGraph(object):

    def __init__(self, nums_node, directed = False):

        self.__nums_node = nums_node
        self.__directed = directed
        self.__nums_edges = 0
        self.__edges = []
        for i in range(nums_node):
            self.__edges.append([None]*nums_node)

    def has_edge(self, orgin, goal):

        if orgin < 0 or orgin >= self.__nums_node or goal < 0 or goal >= self.__nums_node:
            raise IndexError('index out of range')

        return self.__edges[orgin][goal] is not None

    def add_edge(self, orgin, goal, weight):

        if orgin < 0 or orgin >= self.__nums_node or goal < 0 or goal >= self.__nums_node:
            raise IndexError('index out of range')

        if not self.has_edge(orgin, goal):
            self.__nums_edges += 1

        self.__edges[orgin][goal] = Edge(orgin, goal, weight)
        
        if not self.__directed:
            self.__edges[goal][orgin] = Edge(goal, orgin, weight)

    def __str__(self):

        string = ''

        for i in range(self.__nums_node):
            for j in range(self.__nums_node):
                if self.__edges[i][j] is None:
                    string += 'None '
                else:
                    string += '%s ' % str(self.__edges[i][j].weight)
            string += '\n'
        
        return string

    def iter_nodes(self, node):

        if node < 0 or node >= self.__nums_node:
            raise ValueError('index out of range. Fail to get iterator')

        return iter([x for x in self.__edges[node] if x is not None])

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
    wdg = WeightedDenseGraph(nums_node)
    for i in range(1,len(data)):
        orgin, goal, weight = data[i]
        wdg.add_edge(orgin, goal, weight)
    print(wdg)
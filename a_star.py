
class Graph:

    def __init__(self, graph_dict = None, directed = True):
        self.graph_dict = graph_dict or {}

    def connect(self, a, b, distance = 1):
        self.graph_dict.setdefault(a, {})[b] = distance

    def get(self, a, b = None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


class Node:
    def __init__(self, name : str, parent : str):
        self.name = name
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return '({0}, {1})'.format(self.position, self.f)


def astar_search(graph, heuristics, start_id, end_id):
    open = []
    closed = []

    start = Node(start_id, None)
    end = Node(end_id, None)

    open.append(start)
    while len(open) > 0:
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)

        if current_node == end:
            path = []
            while current_node != start:
                path.append(current_node.name + ": " + str(current_node.g))
                current_node = current_node.parent

            path.append(start.name + ": " + str(start.g))
            return path[::-1]

        adj = graph.get(current_node.name)
        for key, value in adj.items():
            adjacent = Node(key, current_node)
            if adjacent in closed:
                continue
            adjacent.g = current_node.g + graph.get(current_node.name, adjacent.name)
            adjacent.h = heuristics.get(adjacent.name)
            adjacent.f = adjacent.g + adjacent.h

            for node in open:
                if adjacent == node and adjacent.f > node.f:
                    continue
            open.append(adjacent)
    return None

def main():

    graph = Graph()

    graph.connect('a', 'b', 3)
    graph.connect('a', 'c', 9)
    graph.connect('a', 'd', 7)
    graph.connect('b', 'f', 100)
    graph.connect('b', 'e', 4)
    graph.connect('c', 'e', 10)
    graph.connect('c', 'g', 6)
    graph.connect('d', 'i', 4)
    graph.connect('e', 'c', 1)
    graph.connect('e', 'f', 8)
    graph.connect('g', 'e', 7)
    graph.connect('i', 'j', 2)

    heuristics = {}
    heuristics['a'] = 0
    heuristics['b'] = 10
    heuristics['c'] = 3
    heuristics['d'] = 7
    heuristics['e'] = 8
    heuristics['f'] = 0
    heuristics['g'] = 14
    heuristics['i'] = 3
    heuristics['j'] = 1
    heuristics['k'] = 2

    path = astar_search(graph, heuristics, 'a', 'f')
    print(path)


if __name__ == '__main__':
    main()

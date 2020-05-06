import sys
import copy

class Node:

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0


    def get_path(self):
        node_list = []
        node = self
        while node is not None:
            node_list.append(node)
            node = node.parent

        path = ""
        for i in range(len(node_list) -1, -1, -1):
            path += node_list[i].__repr__()
        return path


    def compute_heuristic(self, end_node):
        stack_id = {}
        curr_id = 0
        for i in range(len(self.state)):
            for element in self.state[i]:
                stack_id[element] = curr_id
                curr_id += 1

        heuristic_cost = 0
        curr_id = 0
        for i in range(len(end_node.state)):
            for element in end_node.state[i]:
                heuristic_cost += abs(curr_id - stack_id[element])
        return heuristic_cost


    def __repr__(self):
        string = "Current state (top of stack left):\n"

        stack_list = []
        for i in range(len(self.state)):
            stack_string = "["
            for j in range(len(self.state[i])):
                stack_string += str(self.state[i][j])
                if j < len(self.state[i]) - 1:
                    stack_string += " "
            stack_string += "]\n"
            stack_list.append(stack_string)


        for stack_string in stack_list[::-1]:
            string += stack_string
        string += "\n"
        return string
    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __lt__(self, other):
        return self.f < other.f


class Graph:

    def __init__(self, start_config, end_config):
        self.s_config = start_config
        self.e_config = end_config
        self.size = len(start_config)

    def expand(self, node: Node) -> list:

        expand_list = []
        for i in range(self.size):

            if len(node.state[i]) > 0:
                state_copy = copy.deepcopy(node.state)
                aux_node = Node(state_copy, node)
                element = aux_node.state[i].pop(0)

                for j in range(self.size):
                    if i != j:
                        state_new = copy.deepcopy(aux_node.state)
                        next_node = Node(state_new, node)
                        next_node.state[j].insert(0, element)
                        expand_list.append(next_node)
        return expand_list


def astar_search(graph: Graph):

    open = []
    closed = []

    start = Node(graph.s_config, None)
    end = Node(graph.e_config, None)
    open.append(start)

    while len(open) > 0:
        open.sort()
        c_node = open.pop(0)

        if c_node in closed:
            continue

        closed.append(c_node)

        if c_node == end:
            return c_node.get_path()

        neighbours = graph.expand(c_node)
        for next_node in neighbours:
            if next_node in closed:
                continue
            next_node.g = c_node.g + 1
            next_node.h = next_node.compute_heuristic(end)
            next_node.f = next_node.g + next_node.h

            worth_adding = True
            for node in open:
                if next_node == node and next_node.f > node.f:
                    wort_adding = False
                    break

            if worth_adding:
                open.append(next_node)

    return None


if __name__ == "__main__":

    start_config = [["a", "b", "c"], [], []]
    end_config = [["c", "b", "a"], [], []]

    graph = Graph(start_config, end_config)

    result = astar_search(graph)
    print(result)

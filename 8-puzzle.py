import sys
import re
import copy

class EightPuzzle():
    def __init__(self, str):
        pttn = re.compile("(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)")
        result = pttn.match(str)
        if result is not None:
            s = result.groups()
            self.state = [[int(s[0]), int(s[1]), int(s[2])],
                          [int(s[3]), int(s[4]), int(s[5])],
                          [int(s[6]), int(s[7]), int(s[8])]]

    def __str__(self):
        s = ''
        for i in range(0, 3):
            for j in range(0, 3):
                s += str(self.state[i][j]) + ' '
        return s

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        uid = 0
        mult = 1
        for i in range(0, 3):
            for j in range(0, 3):
                uid += self.state[i][j] * mult
                mult *= 9
        return uid

    def manhatten_distance(self, goal):
        sum = 0
        for i in range(0, 3):
            for j in range(0, 3):
                tile = self.state[i][j]
                for m in range(0, 3):
                    for n in range(0, 3):
                        if tile == goal.state[m][n]:
                            sum += abs(i - m) + abs(j + n)
        return sum

    def neighbors(self):
        list = []
        idx = self.get_blank_index()
        x = idx[0]
        y = idx[1]
        if x > 0:
            r = copy.deepcopy(self)
            r.state[y][x] = r.state[y][x - 1]
            r.state[y][x - 1] = 0
            list.append((r, 'r'))
        if x < 2:
            l = copy.deepcopy(self)
            l.state[y][x] = l.state[y][x + 1]
            l.state[y][x + 1] = 0
            list.append((l, 'l'))
        if y > 0:
            d = copy.deepcopy(self)
            d.state[y][x] = d.state[y - 1][x]
            d.state[y - 1][x] = 0
            list.append((d, 'd'))
        if y < 2:
            u = copy.deepcopy(self)
            u.state[y][x] = u.state[y + 1][x]
            u.state[y + 1][x] = 0
            list.append((u, 'u'))
        return list

    def get_blank_index(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == 0:
                    x = j
                    y = i
        return (x, y)

    def a_star(self, goal, heuristic, output):
        closed_set = set()
        open_set = set([self])
        came_from = {}

        g_score = {self: 0}
        f_score = {self: g_score[self] + heuristic(self, goal)}

        while (len(open_set) != 0):
            current = None
            for node in open_set:
                if current is None or f_score[node] < f_score[current]:
                    current = node
            if current == goal:
                return output(self, came_from, current)

            open_set.remove(current)
            closed_set.add(current)

            for n in current.neighbors():
                neighbor = n[0]

                if neighbor in closed_set:
                    continue
                tentative_g_score = g_score[current] + 1

                if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = (current, n[1])
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    if neighbor not in open_set:
                        open_set.add(neighbor)

        return "nil"

    def action_sequence(self, came_from, current_node):
        goal = current_node
        return self.action_sequence_helper(came_from, current_node, goal)

    def action_sequence_helper(self, came_from, current_node, goal):
        delineator = "+"
        if current_node == goal:
            delineator = ""
        if current_node in came_from:
            p = self.action_sequence_helper(came_from, came_from[current_node][0], goal)
            p += came_from[current_node][1] + delineator
            return p
        else:
            return ""

def main():


    heuristic = EightPuzzle.manhatten_distance

    output = EightPuzzle.action_sequence

    input_i = sys.stdin.readline()
    input_f = sys.stdin.readline()

    initial = EightPuzzle(input_i)
    goal = EightPuzzle(input_f)

    print(initial.a_star(goal, heuristic, output))


if __name__ == '__main__':
    main()
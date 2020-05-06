import bintrees

n = 3
m = 2
d = {}

class Nod:
    def __init__(self, h, f = 1000, g = 100000, last = None):
        self.h = h
        self.f = f
        self.g = g
        self.last = last


def heuristic(s):

    left = s[0] + s[1]
    right = n - left

    if s[2] == 0:
        return 2 * (left // m - 1) + 1 # number of needed transports if boat is on left
    else:
        return 2 * (right) // m + 1  # number of need transports if boat is on right


def expand(s):
    sol = []
    # Cannibals

    for i in range(1, min(m, s[0]) + 1):
        if n - s[1] == 0 or n - s[1] >= n - s[0] + i:
            sol.append((n - s[0] + i, n - s[1], 1 - s[2]))

    # Missionaries

    for i in range(1, min(m, s[1]) + 1):
        if (s[1] - i >= s[0] or s[1] - i == 0) and n - s[1] + i >= n - s[0]:
            sol.append((n - s[0], n - s[1] + i, 1 - s[2]))

    # Both types in the boat
    for i in range(1, min(m, s[1]) + 1):
        for j in range(1, min(i, m - i) + 1):
            if s[1] - i >= s[0] - j and n - s[1] + i >= n - s[0] + j:
                sol.append((n - s[0] + j, n - s[1] + i, 1 - s[2]))
    return sol


def Astar(start, end):

    open = bintrees.RBTree()
    in_open = {}
    d[start] = Nod(heuristic(start))
    d[start].f = 0
    d[start].g = 0
    open.insert((d[start].f, start), d[start].f)
    in_open[start] = 1

    while len(open) > 0:

        best = open.pop_min()
        current = best[0][1]
        del in_open[current]

        if current == end:
            return make_path(current)

        successors = expand(current)
        #For any in the expansion list
        for adj in successors:
            if adj not in d:
                d[adj] = Nod(heuristic(adj))

            now_g= d[current].g + 1
            if now_g < d[adj].g:

                d[adj].last = current
                d[adj].g = now_g
                d[adj].f = d[adj].g + d[adj].h

                if adj not in in_open:
                    open.insert((d[adj].f, adj), d[adj].f)
                    in_open[adj] = 1

    return "Nu solution"


def print_fun(sol):
    for x in sol:
        if x[2] == 0:
            print(x[0] ," canibali ", x[1], " misionari ", "barca pe stanga ", n - x[0], " canibali ", n - x[1], " misionari")
        else:
            print(n - x[0], " canibali " , n - x[1], " misionari ", "barca pe dreapta", x[0], " misionari ", x[1], " canibali")


def make_path(current):

    path = []
    while current is not None:
        path.append(current)
        current = d[current].last
    path.reverse()
    return path


if __name__ == "__main__":

    start = (n, n, 0)   #All people on the left
    finish = (n, n, 1)  #All people on the right
    print_fun(Astar(start, finish))
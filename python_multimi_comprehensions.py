
def multimi(list):
    return set([x for x in list if str(x)[0] == str(x)[-1]])


def diagonal(list):
    return sum([list[i][i] for i in range(0,len(list))])



#print(multimi([1, 2, 100, 101, 101]))

print(diagonal([[1, 2], [3, 4]]))
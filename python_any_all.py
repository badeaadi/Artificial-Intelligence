

def list_nr(list):
    return all([x >= 0 and x == int(x) for x in list])


def list_list(list):
    return any([x[0] == x[-1] for x in list])


def mat(list):
    return all([all([x==0] for x in [y for y in list])])


def sir_in_lista(sir, list):
    return any([x in sir for x in list])


print(list_nr([1, 2, -1]))

print(list_list(['12', '23']))

print(mat([[0, 0], [0, 0]]))

print(sir_in_lista('abcde', ['def', 'abc']))
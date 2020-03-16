
class DimError(BaseException):
    pass

#Cerinta 1
def functie_matrice(n, m, elem):
    elem = [[str(i) + str(j) for j in range(m)] for i in range(n)]
    print(elem)

#Cerinta 2
def mat_impar(mat):
    return [mat[i] for i in range(len(mat)) if i % 2]

#Cerinta 3
def mat_per(m1, m2):
    try:
        if not len(m1)==len(m2) and all([len(m1[i])==len(m2[i])] for i in range(len(m1))):
            raise DimError
        m = [[m1[i][j] + m2[i][j] for j in range(len(m1[i]))] for i in range(len(m1))]
        return m

    except DimError:
        pass
    except Exception as error:
        print(error)

elem = []
functie_matrice(3, 3, elem)
print(mat_impar([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))

m1 = [[1, 2], [2, 3, 4], [3, 4, 5]]
m2 = [[-1, -2], [-2, -3, -4], [-3, -4, 5]]
print(mat_per(m1, m2))

#Cerinta 4
def matrice_identitate(n):
    return [[1 if i == j else 0 for i in range(n)] for j in range(n) ]

print(matrice_identitate(5))

#Cerinta 5
def matrice_from_list(l1, l2):
    return [[0 if l1[i] == l2[j] else -1 if (l1[i] < l2[j]) else 1 for i in range(len(l1))] for j in range(len(l2))]

print(matrice_from_list([1, 2, 3], [2, 3, 4]))
l = ["papagal", "pisica","soarece","bolovan","soparla","catel", "pasare"]
#Cerinta 1
mat = []
SIGMA = 26
alph = range(ord("a"), ord("z") + 1)
N = 2

def gen_matrice():
    row = []
    row.append(0)
    for i in alph:
        row.append(chr(i))
    mat.append(row)
    for i in alph:
        row = []
        row.append(chr(i))
        for j in alph:
            row.append(0)
        mat.append(row)
    for i in mat:
        print(i)
gen_matrice()
#Cerinta 2
def completeaza_matrice(l,mat):
    d = {}
    for i in alph:
        for j in alph:
            p = chr(i) + chr(j)
            d[p]=0
    for cuv in l:
        for ch1 in range(0,len(cuv)):
            for ch2 in range(ch1 + 1, len(cuv)):
                p = cuv[ch1] + cuv[ch2]
                d[p] += 1
    for i in alph:
        for j in alph:
            p = chr(j) + chr(i)
            mat[i - ord('a') + 1][j - ord('a') + 1] = d[p]
completeaza_matrice(l,mat)
for i in mat:
    print(i)
#Cerinta 4
for i in range(1, SIGMA + 1):
    for j in range(1, SIGMA + 1):
        if i != j and mat[i][j] > N:
            print("({},{})".format(chr(i + ord('a') - 1),chr(j + ord('a') - 1)))
#Cerinta 3
to_del = []
for i in range(1, SIGMA + 1):
    nr = 0
    for j in range(1, SIGMA + 1):
        if mat[i][j]==0:
            nr += 1
    if nr == SIGMA:
        to_del.append(mat[i])
for i in to_del:
    mat.remove(i)
to_del = []
for i in range(1,27):
    nr = 0
    for j in range(1,len(mat)):
        if mat[j][i]==0:
            nr += 1
    if nr==len(mat)-1:
        to_del.append(i)
to_del.reverse()
for i in to_del:
    for j in range(0,len(mat)):
        del mat[j][i]
for i in mat:
    print(i)
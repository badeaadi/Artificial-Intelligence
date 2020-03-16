

l = [102, 2, 5, 6, 9, 151]
def sortare_sir(l):
    l.sort(key=lambda x: str(x))

def sortare_sir_reverse(l):
    l.sort(key=lambda x: str(x), reverse=True)

def sortare_lung(l):
    l.sort(key=lambda x: len(str(x)))

def sortare_nr_cifre_dist(l):
    l.sort(key=lambda x: set(str(x)))

sortare_sir(l)
print(l, sep = ' ')
sortare_sir_reverse(l)

sortare_nr_cifre_dist(l)
print(l, sep = ' ')


exp = ["5*10","1+2+3","2-5","3+4"]

def sortare_expresie(exp):
    exp.sort(key= lambda x: eval(x))
    #print(sorted(exp,key=lambda x:eval(x)))

sortare_expresie(exp)
print(exp, sep=' ')
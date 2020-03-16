import string

#Cerinta 1
l = [x for x in range(1, 10, 2)]
print(l)

#Cerinta 2
a = [x for x in string.ascii_lowercase]
print(a)

#Cerinta 3
def plus_minus(n):
    l = [-x if x%2==0 else x for x in range(1,n)]
    return l


#Cerinta 4
def impar(list):
    return [x for x in list if x%2 == 1]

#Cerinta 5
def list_poz_impar(list):
    return [list[x] for x in range(0 , len(list) , 2)]


#Cerinta 6
def list_proc(list):
    return [list[x] for x in range(0 , len(list)) if x%2 == list[x]%2]

#Cerinta 7
def list_per(list):
    return [(list[x], list[x + 1]) for x in range(0 , len(list)-1)]

#Cerinta 8
def gen_liste(n):
    return [[x * y for x in range(1, n + 1, 1)] for y in range(1, n + 1, 1)]

#Cerinta 9
def rotate_string(str):
    return [str[x:] + str[:x] for x in range(0, len(str), 1)]

print(rotate_string("abcde"))

#Cerinta 10
def gen_liste_mari(n):
    return [[y for x in range(0, y)] for y in range(0, n + 1)]

print(gen_liste_mari(3))
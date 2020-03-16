
#Cerinta 1

def functie_dict_prim(n1, n2):
    m = {i : [j for j in range(1,i+1) if i%j==0] for i in range(n1, n2 + 1)}
    print(m)


#Cerinta 2
def functie_lista(list):
    return {sum(list[i]): list[i] for i in range(len(list))}

list = [[5,9,1],[2,3],[5,3,0,7],[1,4,3,0,8]]
print(functie_lista(list))


#Cerinta 3
def functie_dictionar_liste(list):
     return {list[i]: [x for x in range(min(list[i]) + 1, max(list[i])) if x not in list[i]] for i in range(0, len(list))}


l = [(3,7,9),(1,2,3,4),(10,3,5,6),(2,2),(6,7,1,2,4)]
print(functie_dictionar_liste(l))

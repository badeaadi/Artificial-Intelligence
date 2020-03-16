l = ["margareta", "crin","crizantema","lalea","zorea" , "violeta", "orhidee","trandafir","crin","zorea","gerbera" , "iasomie","iris","crin","zorea","tractor", "zambila", "mimoza"]

def add_delete():
    command = input("insert comand")
    c,w = command.split('#')
    if c=="del":
        if w in l:
            l.remove(w)
        else:
            print("Cuvantul nu a fost gasit\n")
    else:
        l.reverse()
        l.append(w)
        l.reverse()

#add_delete()
#print(lst)

def replace_list(l,cuv):

    cuv=cuv.replace("("," ")
    cuv=cuv.replace(")"," ")
    cuv=cuv.strip()

    first=0
    second=0
    for i in range(0, len(l)):
        if l[i] == cuv and first == 0:
            first = i
        elif l[i] == cuv and second == 0:
            second = i

    aux= l[first+1:second]
    aux.reverse()
    l[first+1:second] = aux
    print(l)

replace_list(l,"((crin))")
print(l)

def creare_lista(c1,c2,lst):
    res=[]
    for word in lst:
        if word.startswith(c1) and word.endswith(c2):
            res.append(word)
    return res

print(creare_lista("z", "a", l))

def sort_list(lst):
    print(sorted(lst))

#sort_list(lst)
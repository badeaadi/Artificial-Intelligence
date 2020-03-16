import string
sir='Candva, demult, acum 1000 de ani traia o printesa intr-un castel. Si printesa intr-o zi auzi cum aparuse pe meleagurile sale un cufar fermecat din care iesea grai omenesc. Printesa curioasa strabatu 7 ulite si 7 piete; ajunse la cufar si vazu ca toti stateau la 100 metri distanta de el si se mirau. Din cufar intr-adevar se auzeau vorbe nedeslusite. Printesa curajoasa se duse sa-i vorbeasca. Il intreba cine e si ce dorinte are. Raspunsul fu: \"Sunt Ion am cazut in cufar si m-am ferecat din gresala. As dori sa ies.\". Printesa deschise cufarul si-l elibera pe Ion. "Multumesc" spuse Ion. Si astfel, povestea cufarului fermecat a fost deslusita.'

#print(len(sir))


def numar_caractere(s):
    return len(s)

def nealfanumeric(s):
    nealf = 0
    new_s = []
    for ch in s:
        if not ch.isalnum() and ch != '-':
            new_s.append(ch)
    return new_s

def tokens(sir):
    sep = nealfanumeric(sir)
    uniq = [x for x in set(sep)]
    first_sep = uniq[0]

    for s in uniq[1:]:
        sir=sir.replace(s,first_sep)

    res = [i.strip() for i in sir.split(first_sep)]

    return res

def cuvinte_masculin(tokens):
    res=[]
    for word in tokens:
        if word.endswith("ul"):
            res.append(word)
    return res

def cuvinte_cratima(tokens):
    res=[]
    for word in tokens:
        if "-" in word:
            res.append(word)
    return res

print((nealfanumeric(sir)))

cuv = tokens(sir)
print(cuv)
print(cuvinte_masculin(cuv))
print(cuvinte_cratima(cuv))
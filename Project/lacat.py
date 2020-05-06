import copy
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
import sys
import time


class Nod:
    # retinem datele unui nod
    def __init__(self, stare, tata, cheie=None):
        self.stare = stare
        self.tata = tata
        self.cheie = cheie
        self.g = -1  # Distance from initial state to current state
        self.h = -1  # Estimate to the final state
        self.f = -1  # Sum of g and h
        self.mutari = -1

    def __eq__(self, alt_nod):
        return self.stare == alt_nod.stare and self.f == alt_nod.stare

    def __lt__(self, alt_nod):
        return self.f < alt_nod.f or (self.f == alt_nod.f and self.stare < alt_nod.stare)

    def __hash__(self):
        valoare_hash = int(self.f)
        for element in self.stare:
            valoare_hash = valoare_hash * 31 + element
        return valoare_hash


#  2 3 0 1 2 4 2

# intoarcem valoarea medie a numarului de incuieri
def euristica_medie(stare):
    suma = 0
    for element in stare:
        suma += element
    return suma / len(stare)


# Value of smallest element
def euristica_minima(stare):
    valoare = 0
    for element in stare:
        if element != 0:
            if valoare == 0 or element < valoare:
                valoare = element
    return valoare


# Sum of values from the list
def euristica_suma(stare):
    suma = 0
    for element in stare:
        suma += element
    return suma


def genereaza_succesori(nod, lista_chei, euristica):
    succesori = []
    for cheie in lista_chei:
        # Genertae the new state
        stare_noua = copy.deepcopy(nod.stare)

        for i in range(len(cheie)):
            if cheie[i] == 'd':
                stare_noua[i] = max(stare_noua[i] - 1, 0)
            elif cheie[i] == 'i':
                stare_noua[i] += 1

        nod_nou = Nod(stare_noua, nod, cheie)

        # calculam valorile lui g, h si f pentru nodul creat, cat si numarul de mutari de la starea initiala
        nod_nou.g = nod.g + 1
        nod_nou.h = euristica(nod_nou.stare)
        nod_nou.f = nod_nou.g + nod_nou.h
        nod_nou.mutari = nod.mutari + 1
        succesori.append(nod_nou)

    return succesori


# functia care ruleaza algoritmul A*
def astar(stare_initiala, stare_finala, euristica, lista_chei):
    nod_initial = Nod(stare_initiala, None, None)
    deschise = SortedSet([nod_initial])
    scor_optim = SortedDict({tuple(stare_initiala): 0})

    # [1, 1, 1, 1, 1]
    # (1, 1, 1, 1, 1)

    while len(deschise) > 0:
        # extragem nodul cu f minim
        nod = deschise[0]
        deschise.pop(0)

        # daca am ajuns la starea finala, ne oprim
        if nod.stare == stare_finala:
            return nod

        # generam succesorii si facem verificari
        lista_succesori = genereaza_succesori(nod, lista_chei, euristica)
        for succesor in lista_succesori:
            if scor_optim.__contains__(tuple(succesor.stare)) == False:
                # daca starea succesorului nu a mai fost intalnita pana acum, o inseram
                scor_optim[tuple(succesor.stare)] = succesor.g
                deschise.add(succesor)
            elif succesor.g < scor_optim[tuple(succesor.stare)]:
                # introducem/editam starea curenta in setul "deschis", dupa caz
                succesor_fals = Nod(succesor.stare, None, None)
                succesor_fals.f = scor_optim[tuple(succesor.stare)] + euristica(succesor.stare)

                if deschise.__contains__(succesor_fals) is True:
                    deschise.discard(succesor)
                deschise.add(succesor)
                # daca starea curenta este intalnita cu un cost mai mic, o reactualizam
                scor_optim[tuple(succesor.stare)] = succesor.g

    return None


def citeste_chei(fisier_chei):
    lista_chei = []
    for linie in fisier_chei.readlines():
        lista_chei.append(linie[:-1])
    return lista_chei


def verifica_validitate(dimensiune, lista_chei):
    for i in range(dimensiune):
        gasit = False
        for cheie in lista_chei:
            if cheie[i] == 'd':
                gasit = True
        if gasit is False:
            return False
    return True


def afiseaza_raspuns(nod_final, nume_fisier):
    fisier = open(nume_fisier, 'w')

    # reconstruim lista de noduri
    lista_noduri = []
    while nod_final is not None:
        lista_noduri.append(nod_final)
        nod_final = nod_final.tata

    # iteram lista in sens invers
    for nod in lista_noduri[::-1]:
        if nod.cheie is not None:
            fisier.write('Folosim cheia ' + nod.cheie + '. ')
        fisier.write('Suntem in starea [')
        for i in range(len(nod.stare)):
            fisier.write('inc(')
            if nod.stare[i] == 0:
                fisier.write('d, 0)')
            else:
                fisier.write('i, ' + str(nod.stare[i]) + ')')

            if i < len(nod.stare) - 1:
                fisier.write(', ')
            else:
                fisier.write(']')
        fisier.write('\n')
    fisier.close()


if __name__ == '__main__':

    #dimensiune = 7
    #fisier_chei = open("input_1.in", 'r')

    dimensiune = int(sys.argv[1])
    fisier_chei = open(sys.argv[2], 'r')

    lista_chei = citeste_chei(fisier_chei)

    verdict = verifica_validitate(dimensiune, lista_chei)
    if verdict is False:
        print('Setul de chei nu poate sa deschida incuietoarea.')
        sys.exit(0)

    stare_initiala = [1 for i in range(dimensiune)]
    stare_finala = [0 for i in range(dimensiune)]

    t0 = time.time()
    nod_final_1 = astar(stare_initiala, stare_finala, euristica_minima, lista_chei)
    t1 = time.time()
    print('Prima euristica a rulat timp de ' + str(round(t1 - t0, 4)) + ' secunde.')

    t0 = time.time()
    nod_final_2 = astar(stare_initiala, stare_finala, euristica_medie, lista_chei)
    t1 = time.time()
    print('A doua euristica a rulat timp de ' + str(round(t1 - t0, 4)) + ' secunde.')

    t0 = time.time()
    nod_final_3 = astar(stare_initiala, stare_finala, euristica_suma, lista_chei)
    t1 = time.time()
    print('A treia euristica a rulat timp de ' + str(round(t1 - t0, 4)) + ' secunde.')

    afiseaza_raspuns(nod_final_1, '1.out')
    afiseaza_raspuns(nod_final_2, '2.out')
    afiseaza_raspuns(nod_final_3, '3.out')

    fisier_chei.close()

class Elev:

    id_current = 1

    def __init__(self, nume, sanatate = 90, inteligenta = 20, oboseala = 0, buna_dispozitie = 100):

        if len(nume) == 0:
            nume = "Necunoscut" + str(Elev.id_current)
            Elev.id_current += 1

        self.nume = nume
        self.sanatate = sanatate
        self.inteligenta = inteligenta
        self.oboseala = oboseala
        self.buna_dispizitie = buna_dispozitie

    def desfasoara_activitate(self, activitate):

    def trece_ora(self):

    def


class Activity:
    def __init__(self, nume, factor_sanatate, factor_inteligenta, factor_oboseala, factor_dispozitie, durata):
        if len(nume) == 0:
            nume = "Necunoscut" + str(Elev.id_current)
            Elev.id_current += 1

        self.nume = nume
        self.factor_sanatate = factor_sanatate
        self.factor_inteligenta = factor_inteligenta
        self.factor_oboseala = factor_oboseala
        self.factor_dispizitie = factor_dispozitie
        self.durata = durata


act = []
fisier = open("activitati.txt", "r")
for linie in fisier:
    all = linie.split()
    new_activity = Activity(all[0], int(all[1]), int(all[2]), int(all[3]), int(all[4]), int(all[5]))
    act.append(new_activity)

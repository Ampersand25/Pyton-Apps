class Produs:
    def __init__(self, id, denumire, pret):
        #metoda care instantiaza un obiect de clasa Produs
        #date de intrare: id - int (numar intreg)
        #                 denumire - str (string = sir de caractere)
        #                 pret - float (numar real/floating point)
        #date de iesire: -

        self.__id = id
        self.__denumire = denumire
        self.__pret = pret

    #getters
    def get_id(self):
        #metoda de tip getter care returneaza campul id al unui obiect de clasa Produs
        #date de intrare: -
        #date de iesire: int (campul id al obiectului)

        return self.__id

    def get_denumire(self):
        #metoda de tip getter care returneaza campul denumire al unui obiect de clasa Produs
        #date de intrare: -
        #date de iesire: str (campul denumire al obiectului)

        return self.__denumire

    def get_pret(self):
        #metoda de tip getter care returneaza campul pret al unui obiect de clasa Produs
        #date de intrare: -
        #date de iesire: float (campul pret al obiectului)

        return self.__pret

    #setters
    def set_denumire(self, denumire_noua):
        #metoda care actualizeaza campul denumire al unui obiect de clasa Produs
        #date de intrare: denumire_noua - str
        #date de iesire: -

        self.__denumire = denumire_noua

    def set_pret(self, pret_nou):
        #metoda care modifica campul pret al unui obiect de clasa Produs
        #date de intrare: pret_nou - float
        #date de iesire: -

        self.__pret = pret_nou

    def __str__(self):
        #metoda care afiseaza un obiect de clasa Produs ca si string
        #date de intrare: -
        #date de iesire: str (string = sir de caractere)

        return str(self.__id) + ',' + self.__denumire + ',' + str(self.__pret) + '\n'

    def __eq__(self, ot):
        #date de intrare: ot - obiect de clasa Produs
        #date de iesire: bool (tip de data boolean, adica False sau True)
        #postconditii: valoarea returnata de functie este True daca cele doua obiecte au acelasi id, respectiv False in caz contrar

        return self.__id == ot.__id
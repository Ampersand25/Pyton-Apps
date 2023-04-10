class Imobil:
    def __init__(self, id, adresa, pretDorit, tipOferta):
        #instantiatorul unui obiect de clasa Imobil
        #date de intrare: id - numar intreg fara semn (pozitiv, >= 0)
        #                 adresa - sir de caractere (string) nevid
        #                 pretDorit - numar intreg (natural, fara semn)
        #                 tipOferta - sir de caractere (string) nevid
        #date de iesire: obiect de clasa Imobil cu campurile private id, adresa, pretDorit, tipOferta

        self.__id = id
        self.__adresa = adresa
        self.__pretDorit = pretDorit
        self.__tipOferta = tipOferta

    def get_id(self):
        #metoda getter pentru obtinerea campului id al unui obiect Imobil
        #date de intrare: -
        #date de iesire: id - numar natural

        return self.__id

    def get_adresa(self):
        #metoda getter pentru obtinerea campului adresa al unui obiect Imobil
        #date de intrare: -
        #date de iesire: adresa - sir de caractere (string)

        return self.__adresa

    def get_pretDorit(self):
        #metoda getter pentru obtinerea campului pretDorit al unui obiect Imobil
        #date de intrare: -
        #date de iesire: pretDorit - numar natural

        return self.__pretDorit

    def get_tipOferta(self):
        #metoda getter pentru obtinerea campului tipOferta al unui obiect Imobil
        #date de intrare: -
        #date de iesire: tipOferta - sir de caractere (string)

        return self.__tipOferta

    def set_adresa(self, adresa_noua):
        #metoda setter pentru a updata campul privat adresa al unui obiect Imobil
        #date de intrare: adresa_nou - string
        #date de iesire: -

        self.__adresa = adresa_noua

    def set_pretDorit(self, pretDorit_nou):
        #metoda setter pentru a actualiza campul privat pretDorit al unui obiect Imobil
        #date de intrare: pretDorit_nou - numar intreg (int = integer)
        #date de iesire: -

        self.__pretDorit = pretDorit_nou

    def set_tipOferta(self, tipOferta_noua):
        #metoda setter pentru a actualiza campul privat tipOferta al unui obiect Imobil
        #date de intrare: tipOferta_noua - string
        #date de iesire: -

        self.__tipOferta = tipOferta_noua

    def __str__(self):
        #metoda care returneaza modul de afisare al unui obiect de clasa Imobil pentru care se apeleaza metoda (functia)
        #date de intrare: -
        #date de iesire: string care contine toate campurile obiectului de clasa Imobil pentru care se apeleaza (atribute separate prin delimitatorul ',')

        return str(self.__id) + ',' + self.__adresa + ',' + str(self.__pretDorit) + ',' + self.__tipOferta + '\n'

    def __eq__(self, other):
        #metoda care compara doua obiecte de clasa Imobil (self - obiectul pentru care se face apelul si other - obiectul dat ca si parametru de intrare pentru metoda la apel)
        #date de intrare: other - obicet de clasa Imobil
        #date de iesire: True - cele doua obiecte (self si other) au acelasi id (aceeasi valoare in campurile private id din cadrul clasei)
        #                False - in caz contrar

        return self.__id == other.__id
from domeniu.entitate_produs import Produs

class ServiceProduse:
    def __init__(self, valid_produs, repo_produse):
        #instantiere obiect de clasa ServiceProduse

        self.__valid_produs = valid_produs
        self.__repo_produse = repo_produse

    def get_lista_produse(self):
        lista_produse = self.__repo_produse.get_all()
        return lista_produse

    def adauga_produs(self, id_produs, denumire, pret):
        produs = Produs(id_produs, denumire, pret)
        self.__valid_produs.valideaza(produs)
        self.__repo_produse.adauga(produs)

    def __contine_cifra(self, n, cif):
        #metoda care returneaza daca un numar n (intreg) contine sau nu cifra cif
        #date de intrare: n - int
        #preconditii: n >= 0
        #date de iesire: cif - int
        #postconditii: 0 <= cif <= 9

        while n:
            if n % 10 == cif:
                return True
            n //= 10
        return False

    def sterge_produse(self, cifra):
        lista_produse = self.__repo_produse.get_all()
        nr_produse_sterse = 0
        for produs in lista_produse:
            if self.__contine_cifra(produs.get_id(), cifra):
                self.__repo_produse.sterge(produs.get_id())
                nr_produse_sterse += 1
        return nr_produse_sterse

    def filtrare_produse(self, text, numar):
        if text == '' and numar == -1:
            return None
        lista_filtrata = []
        lista_produse = self.__repo_produse.get_all()
        for produs in lista_produse:
            if text != '' and numar != -1:
                #filtrare si dupa denumire si dupa pret
                if text in produs.get_denumire() and produs.get_pret() < numar:
                    lista_filtrata.append(produs)
            elif text == '':
                #filtrare doar dupa pret
                if produs.get_pret() < numar:
                    lista_filtrata.append(produs)
            else: #elif numar == -1:
                #filtrare daor dupa denumire
                if text in produs.get_denumire():
                    lista_filtrata.append(produs)
        return lista_filtrata
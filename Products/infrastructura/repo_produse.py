from erori.exceptii import RepoError

class RepositoryProduse:
    def __init__(self):
        #metoda care instantiaza un obiect de clasa Produs
        #date de intrare: -
        #date de iesire (rezultate): -

        self._produse = []

    def adauga(self, produs_nou):
        #metoda care adauga un obiect de clasa Produs la lista de produse din repo
        #date de intrare: produs_nou - obiect de clasa Produs
        #date de iesire: -
        #metoda arunca (ridica) exceptie de tipul RepoError daca produsul produs_nou exista deja in repo

        for produs in self._produse:
            if produs == produs_nou:
                raise RepoError('produs deja existent!\n')
        self._produse.append(produs_nou)

    def cauta_dupa_id(self, id_produs):
        #metoda care returneaza produsul cu id-ul id_produs daca il gaseste in repo sau arunca exceptie in caz contrar
        #date de intrare: id_produs - intreg
        #preconditii: id_produs >= 0
        #rezultate: obiect de clasa Produs, daca produsul gasit are id-ul egal cu id_produs
        #           RepoError, daca nu exista niciun produs cu id-ul id_produs in repo
        #postconditii: (fie pr obiectul returnat de metoda) => pr.get_id() == id_produs
        #metoda arunca exceptie de tipul RepoError cu mesajul 'produs inexistent!\n' daca nu exista un produs cu id-ul id_produs in lista din repo

        for produs in self._produse:
            if produs.get_id() == id_produs:
                return produs
        raise RepoError('produs inexistent!\n')

    def modifica(self, produs_nou):
        #metoda care modifica produsul cu id-ul produs_id.get_id()
        #date de intrare: produs_nou - obiect de clasa Produs
        #date de iesire: -
        #metoda arunca exceptie de tipul RepoError (Exception) daca nu exista niciun produs cu id-ul produs_nou.get_id() in repo

        for idx in range(len(self._produse)):
            if self._produse[idx] == produs_nou:
                self._produse[idx].set_denumire(produs_nou.get_denumire())
                self._produse[idx].set_pret(produs_nou.get_pret())
                return
        raise RepoError('produs inexistent!\n')

    def sterge(self, id_produs):
        #metoda care sterge produsul cu id-ul id_produs din repo sau arunca exceptie daca nu il gaseste
        #date de intrare: id_produs - int
        #date de iesire: - (nimic)
        #metoda arunca exceptie de tipul RepoError (Exception) daca nu exista niciun produs cu id-ul id_produs in repo

        for idx in range(len(self._produse)):
            if self._produse[idx].get_id() == id_produs:
                del self._produse[idx]
                return
        raise RepoError('produs inexistent!\n')

    def get_all(self):
        #metoda care returneaza o copie shallow a listei de produse din repo
        #date de intrare: - (nimic)
        #date de iesire: o lista (lista de obiecte de clasa Produs)

        return self._produse[:]

    def __len__(self):
        #metoda care furnizeaza numarul de produse din repository
        #date de intrare: nimic
        #date de iesire: int (integer = intreg), numarul de obiecte de clasa Produs din repo

        return len(self._produse)
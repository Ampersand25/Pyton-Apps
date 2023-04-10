from erori.exceptii import RepoError

class RepositoryImobile:
    def __init__(self):
        #date de intrare: -
        #date de iesire: obiect de clasa RepositoryImobile

        self._imobile = []

    def adauga(self, imobil_nou):
        #date de intrare: imobil_nou - obiect de clasa Imobil
        #date de iesire: -

        if imobil_nou in self._imobile:
            raise RepoError('imobil deja existent!\n')
            return
        self._imobile.append(imobil_nou)

    def cauta_dupa_id(self, id_imobil):
        #date de intrare: id_imobil - numar intreg
        #date de iesire: imobilul cu id_imobil daca exista
        #                exceptie de tipul RepoError in caz contrar

        for imobil in self._imobile:
            if imobil.get_id() == id_imobil:
                return imobil
        raise RepoError('imobil inexistent!\n')

    def modifica(self, imobil_nou):
        #date de intrare: imobil_nou - obiect de clasa Imobil
        #date de iesire: RepoError - daca nu exista obiecul de clasa Imobil imobil_nou in repo (adica nu exista un imobil care sa aiba acelasi id cu imobil_nou)
        #                -, in caz contrar

        for idx in range(len(self._imobile)):
            if self._imobile[idx] == imobil_nou:
                self._imobile[idx].set_adresa(imobil_nou.get_adresa())
                self._imobile[idx].set_pretDorit(imobil_nou.get_pretDorit())
                self._imobile[idx].set_tipOferta(imobil_nou.get_tipOferta())
                return
        raise RepoError('imobil inexistent!\n')

    def sterge(self, id_imobil):
        #date de intrare: id_imobil - numar intreg
        #date de iesire: RepoError - daca nu exista imobil cu id-ul id_imobil in repo
        #                -, in caz contrar

        for idx in range(len(self._imobile)):
            if self._imobile[idx].get_id() == id_imobil:
                del self._imobile[idx]
                return
        raise RepoError('imobil inexistent!\n')

    def get_all(self):
        #date de intrare: -
        #date de iesire: o copie shallow a listei de imobile din repository

        return self._imobile[:]

    def __len__(self):
        #date de intrare: -
        #date de iesire: numarul de imobiliare din repo (lungimea listei de imobiliare din repo)

        return len(self._imobile)
from infrastructura.repo_produse import RepositoryProduse
from domeniu.entitate_produs import Produs

class FileRepositoryProduse(RepositoryProduse):
    def __init__(self, filename):
        self.__filename = filename
        RepositoryProduse.__init__(self)

    def __citeste_tot_fisier(self):
        with open(self.__filename, 'r') as f:
            self._produse = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != '':
                    args = line.split(',')
                    produs = Produs(int(args[0]), args[1], float(args[2]))
                    self._produse.append(produs)

    def __append_produs_fisier(self, produs):
        with open(self.__filename, 'a') as f:
            str_produs = str(produs.get_id()) + ',' + produs.get_denumire() + ',' + str(produs.get_pret()) + '\n'
            f.write(str_produs)

    def __scrie_tot_fisier(self):
        with open(self.__filename, 'w') as f:
            for produs in self._produse:
                str_produs = str(produs.get_id()) + ',' + produs.get_denumire() + ',' + str(produs.get_pret()) + '\n'
                f.write(str_produs)

    def adauga(self, produs_nou):
        self.__citeste_tot_fisier()
        RepositoryProduse.adauga(self, produs_nou)
        self.__append_produs_fisier(produs_nou)

    def cauta_dupa_id(self, id_produs):
        self.__citeste_tot_fisier()
        return RepositoryProduse.cauta_dupa_id(self, id_produs)

    def modifica(self, produs_nou):
        self.__citeste_tot_fisier()
        RepositoryProduse.modifica(self, produs_nou)
        self.__scrie_tot_fisier()

    def sterge(self, id_produs):
        self.__citeste_tot_fisier()
        RepositoryProduse.sterge(self, id_produs)
        self.__scrie_tot_fisier()

    def get_all(self):
        self.__citeste_tot_fisier()
        return RepositoryProduse.get_all(self)

    def __len__(self):
        self.__citeste_tot_fisier()
        return RepositoryProduse.__len__(self)
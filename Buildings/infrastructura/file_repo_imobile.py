from domeniu.imobil_entitate import Imobil
from infrastructura.repo_imobile import RepositoryImobile

class FileRepositoryImobile(RepositoryImobile):
    def __init__(self, filename):
        self.__filename = filename
        RepositoryImobile.__init__(self)

    def __citeste_tot_din_fisier(self):
        with open(self.__filename, 'r') as f:
            self._imobile = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != '':
                    argumente = line.split(',')
                    imobil = Imobil(int(argumente[0]), argumente[1], int(argumente[2]), argumente[3])
                    self._imobile.append(imobil)

    def __append_imobil_fisier(self, imobil):
        with open(self.__filename, 'a') as f:
            f.write(str(imobil.get_id()) + ',' + imobil.get_adresa() + ',' + str(imobil.get_pretDorit()) + ',' + imobil.get_tipOferta() + '\n')

    def __scrie_tot_in_fisier(self):
        with open(self.__filename, 'w') as f:
            for imobil in self._imobile:
                f.write(str(imobil.get_id()) + ',' + imobil.get_adresa() + ',' + str(imobil.get_pretDorit()) + ',' + imobil.get_tipOferta() + '\n')

    def adauga(self, imobil_nou):
        self.__citeste_tot_din_fisier()
        RepositoryImobile.adauga(self, imobil_nou)
        self.__append_imobil_fisier(imobil_nou)

    def cauta_dupa_id(self, id_imobil):
        self.__citeste_tot_din_fisier()
        return RepositoryImobile.cauta_dupa_id(self, id_imobil)

    def modifica(self, imobil_nou):
        self.__citeste_tot_din_fisier()
        RepositoryImobile.modifica(self, imobil_nou)
        self.__scrie_tot_in_fisier()

    def sterge(self, id_imobil):
        self.__citeste_tot_din_fisier()
        RepositoryImobile.sterge(self, id_imobil)
        self.__scrie_tot_in_fisier()

    def get_all(self):
        self.__citeste_tot_din_fisier()
        return RepositoryImobile.get_all(self)

    def __len__(self):
        self.__citeste_tot_din_fisier()
        return RepositoryImobile.__len__(self)
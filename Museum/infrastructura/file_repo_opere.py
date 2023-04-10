from infrastructura.repo_opere import RepositoryOpere
from domeniu.opera_entitate import Opera

class FileRepositoryOpere(RepositoryOpere):
    def __init__(self, filename):
        self.__filename = filename
        RepositoryOpere.__init__(self)

    def __citeste_tot_fisier(self):
        with open(self.__filename, 'r') as f:
            self._opere = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != '':
                    arg = line.split(',')
                    opera = Opera(int(arg[0]), arg[1], arg[2], int(arg[3]))
                    self._opere.append(opera)

    def __append_opera_fisier(self, opera):
        with open(self.__filename, 'a') as f:
            f.write(str(opera.get_id()) + ',' + opera.get_denumire() + ',' + opera.get_autor() + ',' + str(opera.get_nr_camera()) + '\n')

    def __scrie_tot_fisier(self):
        with open(self.__filename, 'w') as f:
            for opera in self._opere:
                f.write(str(opera.get_id()) + ',' + opera.get_denumire() + ',' + opera.get_autor() + ',' + str(opera.get_nr_camera()) + '\n')

    def adauga(self, opera):
        self.__citeste_tot_fisier()
        RepositoryOpere.adauga(self, opera)
        self.__append_opera_fisier(opera)

    def cauta_dupa_id(self, id_opera):
        self.__citeste_tot_fisier()
        return RepositoryOpere.cauta_dupa_id(self, id_opera)

    def modifica(self, opera_noua):
        self.__citeste_tot_fisier()
        RepositoryOpere.modifica(self, opera_noua)
        self.__scrie_tot_fisier()

    def sterge(self, id_opera):
        self.__citeste_tot_fisier()
        RepositoryOpere.sterge(self, id_opera)
        self.__scrie_tot_fisier()

    def __len__(self):
        self.__citeste_tot_fisier()
        return RepositoryOpere.__len__(self)

    def get_all(self):
        self.__citeste_tot_fisier()
        return RepositoryOpere.get_all(self)
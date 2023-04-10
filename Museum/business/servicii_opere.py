from infrastructura.repo_opere import RepositoryOpere
from validare.validator_opera import ValidatorOpera
from domeniu.opera_entitate import Opera

class ServiceOpere:
    def __init__(self, valid_opera, repo_opere):
        self.__valid_opera = valid_opera
        self.__repo_opere = repo_opere

    def __criteriu_autor(self, opera):
        return opera.get_autor()

    def raport_1(self, string):
        lista_opere = []
        for opera in self.__repo_opere.get_all():
            if string in opera.get_denumire():
                lista_opere.append(opera)
        lista_opere.sort(reverse = True, key = self.__criteriu_autor)
        return lista_opere

    def raport_2(self, nr_camera):
        lista_autori = []
        for opera in self.__repo_opere.get_all():
            if opera.get_nr_camera() == nr_camera:
                if opera.get_autor() in lista_autori:
                    continue
                lista_autori.append(opera.get_autor())
        return lista_autori
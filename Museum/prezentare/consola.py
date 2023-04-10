from erori.exceptii import ValidError, RepoError
from business.servicii_opere import ServiceOpere

class UI:
    def __ui_raport_1(self):
        string = input('Dati un sir de caractere: ')

        lista_opere = self.__srv_opere.raport_1(string)
        if not len(lista_opere):
            print('Nu exista opere de arta care sa contina stringul', string, 'ca si substring in denumire!\n')
            return

        print('Operele de arta care contin stringul', string, 'ca si substring in denumire (ordonate descrescator dupa autor) sunt:')
        for opera in lista_opere:
            print(opera, end = '')
        print()

    def __ui_raport_2(self):
        try:
            nr_camera = int(input('Dati numarul camerei: '))
        except ValueError as ve:
            print('numar camera invalid!\n')
            return
        except TypeError as te:
            print('numar camera invalid!\n')
            return
        except Exception as ex:
            print('numar camera invalid!\n')
            return

        if nr_camera < 1:
            print('numar camera invalid!\n')
            return

        lista_autori = self.__srv_opere.raport_2(nr_camera)

        if not len(lista_autori):
            print('nu exista numarul dat!\n')
            return

        print('Camera', nr_camera, end = ': ')
        for idx in range(len(lista_autori) - 1):
            print(lista_autori[idx], end = ', ')
        print(lista_autori[len(lista_autori) - 1])
        print()

    def __ui_exit(self):
        print('Iesire din aplicatie...')
        exit()

    def __init__(self, srv_opere):
        self.__srv_opere = srv_opere
        self.__lista_comenzi = {'raport1': self.__ui_raport_1,
                                'raport2': self.__ui_raport_2,
                                'exit': self.__ui_exit}

    def __afiseaza_meniu(self):
        print('Meniu principale:')
        print('raport1 - afisarea tuturor operelor de arta care contin un anumit sir de caractere citit de la tastatura in denumire, ordonate descrescator dupa autor')
        print('raport2 - afisarea tuturor autorilor care au lucrari expuse intr-o camera data (citita de la tastatura)')
        print('exit    - iesirea din aplicatie')

    def ruleaza_aplicatie(self):
        self.__afiseaza_meniu()
        print()
        while True:
            try:
                cmd = input('>>>')
            except ValueError as ve:
                print(str(ve))
                continue
            except TypeError as te:
                print(str(te))
                continue
            except Exception as ex:
                print(str(ex))
                continue
            cmd = cmd.strip()
            if cmd == ' ':
                print()
                continue
            if cmd in self.__lista_comenzi:
                try:
                    self.__lista_comenzi[cmd]()
                except ValueError as ve:
                    print(str(ve))
                    print()
                except TypeError as te:
                    print(str(te))
                    print()
                except ValidError as vae:
                    print(str(vae))
                    print()
                except RepoError as re:
                    print(str(re))
                    print()
                except Exception as ex:
                    print(str(ex))
                    print()
            else:
                print('comanda invalida!\n')
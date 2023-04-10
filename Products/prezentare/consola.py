from erori.exceptii import ValidError, RepoError

class UI:
    def __ui_print_produse(self):
        lista_produse = self.__srv_produse.get_lista_produse()
        if lista_produse == []:
            print('Nu exista inregistrari de produse in magazin!\n')
            return
        print('Lista produselor din magazin este:')
        for idx in range(len(lista_produse)):
            print('Produsul #' + str(idx + 1) + ': ' + str(lista_produse[idx]), end = '')

    def __ui_add_produs(self):
        print('Introduceti datele unui produs')
        try:
            id_produs = int(input('id produs:'))
        except:
            print('id invalid!\n')
            return
        denumire = input('denumire produs: ')
        try:
            pret = float(input('pret produs: '))
        except:
            print('pret invalid!\n')
            return
        self.__srv_produse.adauga_produs(id_produs, denumire, pret)

    def __ui_del_produse(self):
        print('Dati o cifra de la tastatura: ', end = '')
        try:
            cifra = int(input())
        except:
            print('cifra incorect introdusa!\n')
            return
        if cifra < 0 or cifra > 9:
            print('cifra invalida!\n')
            return
        nr_produse_sterse = self.__srv_produse.sterge_produse(cifra)
        print('Au fost sterse in total ' + str(nr_produse_sterse) + ' produse din lista care contin cifra ' + str(cifra) + ' in id!\n')

    def __ui_filtrare_produse(self):
        print('Introduceti criteriile dupa care sa se realizeze filtrarea produselor din magazin')
        text = input('denumire: ')
        try:
            numar = int(input('pret: '))
        except:
            print('numar invalid!\n')
            return
        str_filtru = ''
        if text != '':
            str_filtru += 'denumire'
        if numar != -1:
            if len(str_filtru):
                str_filtru += ' + '
            str_filtru += 'pret'
        if not len(str_filtru): #if str_filtru == '':
            print('Nu s-a introdus niciun criteriu pentru filtrare!\n')
            return
        print('Filtrul curent este: ' + str_filtru)
        produse_filtrate = self.__srv_produse.filtrare_produse(text, numar)
        if not len(produse_filtrate): #if produse_filtrate == []:
            print('Nu exista niciun produs care sa respecte criteriile de filtrare introduse!\n')
            return
        print('Produsele filtrate conform criteriilor de mai sus sunt:')
        idx = 0
        for produs in produse_filtrate:
            idx += 1
            print(str(idx) + ') ' + str(produs), end = '')

    def __ui_undo_stergere(self):
        pass

    def __ui_exit(self):
        print('Iesirea din aplicatie')
        exit()

    def __init__(self, srv_produse):
        self.__srv_produse = srv_produse
        self.__lista_comenzi = {'print_produse': self.__ui_print_produse,
                                'add_produs': self.__ui_add_produs,
                                'del_produse': self.__ui_del_produse,
                                'filtrare_produse': self.__ui_filtrare_produse,
                                'undo_stergere': self.__ui_undo_stergere,
                                'exit': self.__ui_exit}

    def __afisare_meniu(self):
        print('Meniu comenzi aplicatie:')
        print('1 - print_produse    - afiseaza toate produsele din magazin')
        print('2 - add_produs       - adauga un produs in magazin')
        print('3 - del_produse      - sterge toate produsele care contin o cifra data in id-ul lor si afiseaza numarul acestora')
        print('4 - filtrare_produse - filtreaza lista de produse dupa denumire sau/si dupa pret')
        print('5 - undo_stergere    - reface ultima operatie de stergere')
        print('6 - exit             - iesirea din aplicatie (inchide aplicatia)')
        print()

    def ruleaza_aplicatie(self):
        self.__afisare_meniu()
        while True:
            cmd = input('>>>')
            cmd = cmd.strip()
            if cmd == '':
                continue
            cmd = cmd.lower()
            if cmd in self.__lista_comenzi:
                try:
                    self.__lista_comenzi[cmd]()
                    print()
                except ValueError as ve:
                    print(str(ve))
                except TypeError as te:
                    print(str(te))
                except Exception as ex:
                    print(str(ex))
                except ValidError as vae:
                    print(str(vae))
                except RepoError as re:
                    print(str(re))
            else:
                print('comanda invalida!\n')
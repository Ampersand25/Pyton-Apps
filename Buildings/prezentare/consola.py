from erori.exceptii import ValidError, RepoError

class UI:
    def __ui_medie_pret(self):
        try:
            tip_oferta = input('Dati un tip de oferta de la tastatura(vanzare/inchiriere): ')
        except ValueError as ve:
            print(str(ve))
            print()
            return
        except TypeError as te:
            print(str(te))
            print()
            return
        except Exception as ex:
            print(str(ex))
            print()
            return

        medie_pretOferta = self.__srv_rapoarte.medie_pret(tip_oferta)

        if medie_pretOferta != -1:
            print('Media pe pretDorit pentru tipul de oferta', tip_oferta, 'este:', medie_pretOferta)
        else:
            print('Nu exista imobiliare cu tipul de oferta', tip_oferta, end = '!\n')

        print()

    def __ui_efectuare_tranzactie(self):
        try:
            id_proprietate = int(input('Introduceti id-ul unei proprietati de la tastatura: '))
        except ValueError:
            print('id invalid!\n')
            print()
            return
        except TypeError:
            print('id invalid!\n')
            print()
            return
        except Exception:
            print('id invalid!\n')
            print()
            return

        try:
            pret = int(input('Introduceti pretul negociat intre proprietar si cumparator: '))
        except ValueError:
            print('pret invalid!\n')
            print()
            return
        except TypeError:
            print('pret invalid!\n')
            print()
            return
        except Exception:
            print('pret invalid!\n')
            print()
            return

        proprietate = self.__srv_rapoarte.efectuare_tranzactie(id_proprietate, pret)

        if proprietate[0] == '' and proprietate[1] == -1:
            print('Nu exista niciun imobil cu id-ul', id_proprietate, end = '!\n')
            print()
            return

        print('Adresa imobil:', proprietate[0])
        print('Comision aferent tranzactie:', proprietate[1])
        print()

    def __ui_exit(self):
        print('Iesire din aplicatie...')
        exit()

    def __init__(self, srv_rapoarte):
        self.__srv_rapoarte = srv_rapoarte
        self.__comenzi = {'medie_pret'          : self.__ui_medie_pret,
                          'efectuare_tranzactie': self.__ui_efectuare_tranzactie,
                          'exit'                : self.__ui_exit}

    def __afisare_comenzi(self):
        print('Meniu comenzi:')
        print('medie_pret           - calculeaza si afiseaza media pe pret dorit, pentru un tip de oferta dat (vanzare/inchiriere)')
        print('efectuare_tranzactie - efectuarea unei tranzactii')
        print('exit                 - iesirea din aplicatie')

    def ruleaza_aplicatie(self):
        self.__afisare_comenzi()
        print()
        while True:
            try:
                cmd = input('>>>')
            except ValueError as ve:
                print(str(ve))
                print()
                continue
            except TypeError as te:
                print(str(te))
                print()
                continue
            except Exception as ex:
                print(str(ex))
                print()
                continue
            cmd = cmd.strip()
            if cmd == '':
                print()
                continue
            cmd = cmd.lower()
            if cmd in self.__comenzi:
                try:
                    self.__comenzi[cmd]()
                except ValueError as vae:
                    print(str(vae))
                except RepoError as re:
                    print(str(re))
                except ValueError as ve:
                    print(str(ve))
                except TypeError as te:
                    print(str(te))
                except Exception as ex:
                    print(str(ex))
            else:
                print('comanda invalida!\n')
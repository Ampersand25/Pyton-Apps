from erori.exceptii import ValidError

class ServiceRapoarte:
    def __init__(self, repo_imobile):
        #metoda pentru a instantia un obiect de clasa ServiceRapoarte
        #date de intrare: repo_imobile - obiect de clasa FileRepositoryImobile (in cazul nostru) sau RepositoryImobile
        #date de iesire: -

        self.__repo_imobile = repo_imobile

    def medie_pret(self, tip_oferta):
        #metoda care afiseaza media pe pretDorit, pentru un tip de ofertă dat (primul raport/task din lista de functionalitati a aplicatiei)
        #date de intrare: tip_oferta - sir de caractere (string)
        #date de iesire: -1 - nu exista imobil cu tipul de oferta tip_oferta
        #                 media - numar ce reprezinta media pe pretDorit, pentru tipul de data tip_oferta

        tip_oferta = tip_oferta.strip()
        if tip_oferta != 'vanzare' and tip_oferta != 'inchiriere':
            raise ValidError('tip oferta invalid!\n')
        lista_imobile = self.__repo_imobile.get_all()
        sumaPreturi = nrImobile = 0
        for imobil in lista_imobile:
            if imobil.get_tipOferta() == tip_oferta:
                sumaPreturi += imobil.get_pretDorit()
                nrImobile += 1
        if nrImobile:
            return float(sumaPreturi / nrImobile)
        return -1


    def efectuare_tranzactie(self, id_proprietate, pret):
        #metoda care efectueaza o tranzactie (al doilea raport/task din lista de functionalitati a aplicatiei)
        #date de intrare: id_proprietate - numar intreg
        #                 pret - numar intreg
        #date de iesire: o lista de doua valori (prima este adresa - stringul proprietatii cu id-ul id_proprietate iar a doua valoare din lista este comisionul)

        err = ''
        if id_proprietate < 0:
            err += 'id invalid!\n'
        if pret < 0:
            err += 'pret invalid!\n'
        if len(err):
            raise ValidError(str(err))
        lista_imobile = self.__repo_imobile.get_all()
        comision = 0
        for imobil in lista_imobile:
            if imobil.get_id() == id_proprietate:
                if imobil.get_tipOferta() == 'vanzare':
                    comision = float((2 * pret) / 100)
                else:
                    comision = float((50 * pret) / 100)
                return [imobil.get_adresa(), comision]
        return ['', -1]

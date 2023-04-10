from erori.exceptii import ValidError

class ValidatorImobil:
    def valideaza(self, imobil_rau):
        #metoda care valideaza o entitate (obiect) imobil_rau de clasa Imobil
        #date de intrare: imobil_rau - obiectul de clasa Imobil pe care vrem sa il validam (sa ii verificam corectitudinea campurilor)
        #date de iesire: - (nimic), daca obiectul imobil_rau are toate campurile valide
        #                ValidError cu mesajul err in caz contrar

        err = ''
        if imobil_rau.get_id() < 0:
            err += 'id invalid!\n'
        if imobil_rau.get_adresa() == '':
            err += 'adresa invalida!\n'
        if imobil_rau.get_pretDorit() < 0:
            err += 'pret dorit invalid!\n'
        if imobil_rau.get_tipOferta() != 'vanzare' and imobil_rau.get_tipOferta() != 'inchiriere':
            err += 'tip oferta invalid!\n'
        if len(err):
            raise ValidError(str(err))
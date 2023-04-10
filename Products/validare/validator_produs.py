from erori.exceptii import ValidError

class ValidatorProdus:
    def valideaza(self, produs_rau):
        #metoda care valideaza un obiect produs_rau de clasa Produs
        #date de intrare: produs_rau - obiect de clasa Produs
        #date de iesire: -, daca produsul este valid (are campurile corecte)
        #                eroare de tipul ValidError cu mesajul err in cazul in care obiectul nu este valid (are cel putin un camp incorect)
        #metoda/functia ridica/arunca exceptie de tipul ValidError cu mesajul err (err - str/string = sir de caractere) in cazul in care obiectul produs_rau nu este valid

        err = '' #string vid (gol)
        if produs_rau.get_id() < 0:
            err += 'id invalid!\n'
        if produs_rau.get_denumire() == '':
            err += 'denumire invalida!\n'
        if produs_rau.get_pret() < 0:
            err += 'pret invalid!\n'
        if len(err): #exista cel putin o componenta invalida a obiectului
            raise ValidError(str(err)) #ridicam exceptie de tipul ValidError cu mesajul custom (definit) err
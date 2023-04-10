# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from testare.teste import Teste

from validare.validator_imobil import ValidatorImobil

from infrastructura.repo_imobile import RepositoryImobile
from infrastructura.file_repo_imobile import FileRepositoryImobile

from business.servicii_rapoarte import ServiceRapoarte

from prezentare.consola import UI

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    teste = Teste()
    teste.ruleaza_teste()

    valid_imobil = ValidatorImobil()

    filename_imobile = 'imobile.txt'
    file_repo_imobile = FileRepositoryImobile(filename_imobile)

    srv_rapoarte = ServiceRapoarte(file_repo_imobile)

    console = UI(srv_rapoarte)
    console.ruleaza_aplicatie()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

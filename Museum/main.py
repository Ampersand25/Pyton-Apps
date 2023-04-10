# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from testare.teste import Teste

from validare.validator_opera import ValidatorOpera

from infrastructura.repo_opere import RepositoryOpere
from infrastructura.file_repo_opere import FileRepositoryOpere

from business.servicii_opere import ServiceOpere

from prezentare.consola import UI

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    teste = Teste()
    teste.ruleaza_teste()

    valid_opera = ValidatorOpera()

    filename_opere = "opere.txt"
    file_repo_opere = FileRepositoryOpere(filename_opere)

    srv_opere = ServiceOpere(valid_opera, file_repo_opere)

    console = UI(srv_opere)
    console.ruleaza_aplicatie()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

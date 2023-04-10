from testare.teste import Teste
from validare.validator_produs import ValidatorProdus
from infrastructura.file_repo_produse import FileRepositoryProduse
from business.service_produse import ServiceProduse
from prezentare.consola import UI

if __name__ == '__main__':
    teste = Teste()
    teste.ruleaza_teste()

    valid_produs = ValidatorProdus()

    filename = 'produse.txt'
    file_repo_produse = FileRepositoryProduse(filename)

    srv_produse = ServiceProduse(valid_produs, file_repo_produse)

    console = UI(srv_produse)
    console.ruleaza_aplicatie()
from domeniu.entitate_produs import Produs
from erori.exceptii import ValidError, RepoError
from validare.validator_produs import ValidatorProdus
from infrastructura.repo_produse import RepositoryProduse
from business.service_produse import ServiceProduse

class Teste:
    def __ruleaza_teste_entitate(self):
        id_produs, denumire, pret = 6, 'Balsam de par', 4.99
        produs = Produs(id_produs, denumire, pret)
        assert produs.get_id() == id_produs
        assert produs.get_denumire() == denumire
        assert abs(produs.get_pret() - pret) < 1e-5

        produs = Produs(8, 'Cereale', 2.55)
        assert produs.get_id() == 8
        assert produs.get_denumire() == 'Cereale'
        assert abs(produs.get_pret() - 2.55) < 1e-5

    def __ruleaza_teste_validare(self):
        valid_produs = ValidatorProdus()

        produs_bun = Produs(7, 'Supa alfabet', 2.87)
        try:
            valid_produs.valideaza(produs_bun)
            assert True
        except: #except ValidError:
            assert False

        produs_rau = Produs(-4, 'Supa alfabet', 2.87)
        try:
            valid_produs.valideaza(produs_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id invalid!\n'

        produs_rau = Produs(7, '', 2.87)
        try:
            valid_produs.valideaza(produs_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'denumire invalida!\n'

        produs_rau = Produs(7, 'Supa alfabet', -5)
        try:
            valid_produs.valideaza(produs_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'pret invalid!\n'

        produs_rau = Produs(-4, 'Supa alfabet', -5)
        try:
            valid_produs.valideaza(produs_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id invalid!\npret invalid!\n'

        produs_rau = Produs(7, '', -5)
        try:
            valid_produs.valideaza(produs_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'denumire invalida!\npret invalid!\n'

        produs_rau = Produs(-4, '', 2.87)
        try:
            valid_produs.valideaza(produs_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id invalid!\ndenumire invalida!\n'

        produs_rau = Produs(-4, '', -5)
        try:
            valid_produs.valideaza(produs_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id invalid!\ndenumire invalida!\npret invalid!\n'

    def __ruleaza_teste_servicii(self):
        valid_produs = ValidatorProdus()
        repo_produse = RepositoryProduse()
        srv_produse = ServiceProduse(valid_produs, repo_produse)

        #teste adauga_produs
        assert not len(repo_produse.get_all())

        srv_produse.adauga_produs(9, 'Cafea', 5.66)

        assert len(repo_produse.get_all()) == 1

        assert repo_produse.get_all()[0].get_id() == 9
        assert repo_produse.get_all()[0].get_denumire() == 'Cafea'
        assert abs(repo_produse.get_all()[0].get_pret() - 5.66) < 1e-5

        srv_produse.adauga_produs(13, 'Balsam de par', 3)

        assert len(repo_produse.get_all()) == 2

        assert repo_produse.get_all()[0].get_id() == 9
        assert repo_produse.get_all()[0].get_denumire() == 'Cafea'
        assert abs(repo_produse.get_all()[0].get_pret() - 5.66) < 1e-5

        assert repo_produse.get_all()[1].get_id() == 13
        assert repo_produse.get_all()[1].get_denumire() == 'Balsam de par'
        assert abs(repo_produse.get_all()[1].get_pret() - 3) < 1e-5

        try:
            srv_produse.adauga_produs(13, 'Energizant', 7.23)
            assert False
        except RepoError as re:
            assert str(re) == 'produs deja existent!\n'

        assert len(repo_produse.get_all()) == 2

        #teste get_lista_produse
        assert srv_produse.get_lista_produse() == [Produs(9, 'Cafea', 5.66), Produs(13, 'Balsam de par', 3)]
        assert len(srv_produse.get_lista_produse()) == 2

        #teste sterge_produse
        nr = srv_produse.sterge_produse(4)
        assert not nr
        assert len(srv_produse.get_lista_produse()) == 2

        nr = srv_produse.sterge_produse(9)
        assert nr == 1
        assert len(srv_produse.get_lista_produse()) == 1

        nr = srv_produse.sterge_produse(1)
        assert nr == 1
        assert len(srv_produse.get_lista_produse()) == 0

        srv_produse.adauga_produs(26, 'Sarmale cu varza', 6.83)
        srv_produse.adauga_produs(72, 'Boia', 3.35)
        srv_produse.adauga_produs(1, 'Biscuiti cu soia', 7.42)

        #teste filtrare_produse
        l = srv_produse.filtrare_produse('', -1)
        assert l == None

        l = srv_produse.filtrare_produse('cu', -1)
        assert len(l) == 2

        l = srv_produse.filtrare_produse('Biscuiti', -1)
        assert len(l) == 1

        l = srv_produse.filtrare_produse('varza', -1)
        assert len(l) == 1

        l = srv_produse.filtrare_produse('', 5)
        assert len(l) == 1

        l = srv_produse.filtrare_produse('', 7)
        assert len(l) == 2

        l = srv_produse.filtrare_produse('', 8)
        assert len(l) == 3

        l = srv_produse.filtrare_produse('', 2)
        assert len(l) == 0

        l = srv_produse.filtrare_produse('cu', 7)
        assert len(l) == 1

        l = srv_produse.filtrare_produse('cu', 8)
        assert len(l) == 2

        l = srv_produse.filtrare_produse('cu', 1)
        assert len(l) == 0

    def ruleaza_teste(self):
        self.__ruleaza_teste_entitate()
        self.__ruleaza_teste_validare()
        self.__ruleaza_teste_servicii()
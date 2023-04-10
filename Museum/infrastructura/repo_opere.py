from erori.exceptii import RepoError

class RepositoryOpere:
    def __init__(self):
        self._opere = []

    def adauga(self, opera_noua):
        for opera in self._opere:
            if opera == opera_noua:
                raise RepoError('opera deja existenta!\n')
        self._opere.append(opera_noua)

    def cauta_dupa_id(self, id_opera):
        for opera in self._opere:
            if opera.get_id() == id_opera:
                return opera
        raise RepoError('opera inexistenta!\n')

    def modifica(self, opera_noua):
        for idx in range(len(self._opere)):
            if self._opere[idx] == opera_noua:
                self._opere[idx].set_denumire(opera_noua.get_denumire())
                self._opere[idx].set_autor(opera_noua.get_autor())
                self._opere[idx].set_nr_camera(opera_noua.get_nr_camera())
                return
        raise RepoError('opera inexistenta!\n')

    def sterge(self, id_opera):
        for idx in range(len(self._opere)):
            if self._opere[idx].get_id() == id_opera:
                del self._opere[idx]
                return
        raise RepoError('opera inexistenta!\n')

    def get_all(self):
        return self._opere[:]

    def __len__(self):
        return len(self._opere)
from erori.exceptii import ValidError

class ValidatorOpera:
    def valideaza(self, opera_rea):
        err = ''
        if opera_rea.get_id() < 0:
            err += 'id invalid!\n'
        if opera_rea.get_denumire() == '':
            err += 'denumire invalida!\n'
        if opera_rea.get_autor() == '':
            err += 'autor invalid!\n'
        if opera_rea.get_nr_camera() < 1:
            err += 'numar camera invalid!\n'
        if len(err):
            raise ValidError(str(err))
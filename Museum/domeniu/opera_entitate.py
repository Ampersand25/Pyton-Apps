class Opera:
    def __init__(self, id, denumire, autor, nr_camera):
        self.__id = id
        self.__denumire = denumire
        self.__autor = autor
        self.__nr_camera = nr_camera

    def get_id(self):
        return self.__id

    def get_denumire(self):
        return self.__denumire

    def get_autor(self):
        return self.__autor

    def get_nr_camera(self):
        return self.__nr_camera

    def set_denumire(self, denumire_noua):
        self.__denumire = denumire_noua

    def set_autor(self, autor_nou):
        self.__autor = autor_nou

    def set_nr_camera(self, nr_camera_nou):
        self.__nr_camera = nr_camera_nou

    def __str__(self):
        return str(self.__id) + ',' + self.__denumire + ',' + self.__autor + ',' + str(self.__nr_camera) + '\n'

    def __eq__(self, ot):
        return self.__id == ot.__id
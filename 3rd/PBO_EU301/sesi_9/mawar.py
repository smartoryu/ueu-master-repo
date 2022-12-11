from plant import Plant


class Mawar(Plant):
    def __init__(self):
        self.__jenis = "Mawar"

    def cekKondisiTumbuh(self):
        if (self.getJumlahAir() >= 3 & self.getJumlahPupuk() >= 2):
            self.tumbuh()

    def tumbuh(self):
        if (self.__statusTumbuh < 4):
            self.__jumlahAir -= 5
            self.__jumlahPupuk -= 4
            self.__statusTumbuh += 1

    def getJenis(self):
        return self.__jenis

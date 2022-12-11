from plant import Plant


class Melati(Plant):
    def __init__(self):
        self.__jenis = "Melati"

    def cekKondisiTumbuh(self):
        if (self.getJumlahAir() >= 3 & self.getJumlahPupuk() >= 2):
            self.tumbuh()

    def tumbuh(self):
        if (self.__statusTumbuh < 4):
            self.__jumlahAir -= 2
            self.__jumlahPupuk -= 2
            self.__statusTumbuh += 1

    def getJenis(self):
        return self.__jenis

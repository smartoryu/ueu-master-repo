class Plant():
    def __init__(self, __statusTumbuh: int, __jumlahAir: int, __jumlahPupuk: int):
        self.__statusTumbuh = __statusTumbuh
        self.__jumlahAir = __jumlahAir
        self.__jumlahPupuk = __jumlahPupuk

    def setStatusTumbuh(self, __statusTumbuh):
        self.__statusTumbuh = __statusTumbuh

    def setJumlahAir(self, __jumlahAir):
        self.__jumlahAir = __jumlahAir

    def setJumlahPupuk(self, __jumlahPupuk):
        self.__jumlahPupuk = __jumlahPupuk

    def getStatusTumbuh(self): return self.__statusTumbuh

    def getStatusTumbuhText(self):
        match self.__statusTumbuh:
            case 0: return "Benih"
            case 1: return "Tunas"
            case 2: return "Tanaman Kecil"
            case 3: return "Tanaman Dewasa"
            case _: return "Berbunga"

    def getJumlahAir(self): return self.__jumlahAir

    def getJumlahPupuk(self): return self.__jumlahPupuk

    def tumbuh(self):
        if (self.__statusTumbuh < 4):
            self.__jumlahAir -= 3
            self.__jumlahPupuk -= 1
            self.__statusTumbuh += 1

    def cekKondisiTumbuh(self):
        if (self.__jumlahAir >= 3 & self.__jumlahPupuk >= 1):
            self.tumbuh()

    def beriAir(self):
        self.__jumlahAir += 1
        self.cekKondisiTumbuh()

    def beriPupuk(self):
        self.__jumlahPupuk += 1
        self.cekKondisiTumbuh()

    def displayPlant(self):
        print(self.getStatusTumbuhText())
        print(f"Jumlah Air: {self.__jumlahAir}")
        print(f"Jumlah Pupuk: {self.__jumlahPupuk}")

    def getImagePath(self):
        tImagePath = "img/seed.png"
        match self.__statusTumbuh:
            case 0: tImagePath = "img/seed.png"
            case 1: tImagePath = "img/sprout.png"
            case 2: tImagePath = "img/small.png"
            case 3: tImagePath = "img/big.png"
            case 4: tImagePath = "img/blossom.png"
        return tImagePath

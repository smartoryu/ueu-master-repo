class Jam:
    def __init__(self) -> None:
        self.jam = 0
        self.menit = 0
        self.detik = 0

    def tambahJam(self):
        self.jam += 1

    def tambahMenit(self):
        self.menit += 1

    def tambahDetik(self):
        self.detik += 1

    def displayJam(self):
        print(f"{self.jam}:{self.menit}:{self.detik}")


jam1 = Jam()
jam1.tambahJam()
jam1.displayJam()

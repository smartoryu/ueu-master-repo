class Waktu():
    def __init__(self, jam, menit, detik):
        self.jam = jam
        self.menit = menit
        self.detik = detik

    def __formatTime(self):
        time = (self.jam * 3600) + (self.menit * 60) + self.detik
        second = time % 60
        minute = (time // 60) % 60
        hour = (time // 3600) % 24
        return f"{hour} : {minute} : {second}"

    def __formatTimeAsIs(self):
        return f"{self.jam} : {self.menit} : {self.detik}"

    def __str__(self):
        if (self.jam > 24):
            return "Jam tidak valid"
        elif (self.menit > 60):
            return "Menit tidak valid"
        elif (self.detik > 60):
            return "Detik tidak valid"
        else:
            return self.__formatTimeAsIs()


jam = int(input("masukkan jam: "))
menit = int(input("masukkan menit: "))
detik = int(input("masukkan detik: "))

waktu = Waktu(jam, menit, detik)
print(waktu)

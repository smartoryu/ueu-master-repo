from anggrek import Anggrek
from mawar import Mawar
from melati import Melati

ang = Anggrek()
maw = Mawar()
mel = Melati()

while True:
    print("Pilih Tanaman:")
    print("1. Anggrek")
    print("2. Mawar")
    print("3. Melati")
    print("0. Keluar")
    tanaman = int(input("Pilihan: "))
    if (tanaman == 0):
        break

    # print("Masukkan: 0 untuk memberi air, 1 untuk memberi pupuk, 999 untuk keluar")

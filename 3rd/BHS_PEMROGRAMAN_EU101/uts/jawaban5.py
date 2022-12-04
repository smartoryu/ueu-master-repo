menu = ['capucino', 'teh', 'Exit']

while True:
    print('NIM :  1234567')
    print('NAMA :  QWERTY')
    print('Pilihan')
    for i in range(len(menu)):
        print(f'{i+1}. {menu[i]}')
    pilihan = int(input('masukkan pilihan : '))
    if pilihan == 3:
        break
    print(f'memilih {menu[pilihan-1]}')

    harga = int(input('masukkan harga : '))
    print(f'Jumlah yang harus di bayarkan {harga + (0.1 * harga)}')

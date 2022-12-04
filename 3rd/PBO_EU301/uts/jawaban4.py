menu = ['capucino', 'teh', 'Exit']

print('NIM :  1234567')
print('NAMA :  QWERTY')
print('Pilihan')
for i in range(len(menu)):
    print(f'{i+1}. {menu[i]}')
pilihan = int(input('masukkan pilihan : '))

if pilihan != 3:
    print(f'memilih {menu[pilihan-1].upper()}')
    harga = int(input('masukkan harga : '))
    print(harga + (0.1 * harga))

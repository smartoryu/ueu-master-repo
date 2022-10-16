def calculateTax(total):
    return total * 0.1


total = float(input('Masukkan total pembelian: '))
tax = calculateTax(total)

print(
    f"{'Pembelian:':20}{total:20,.0f}",
    f"\n{'PPN (10%):':20}{tax:20,.0f}",
    f"\n{'Total Pembayaran:':20}{(total + tax):20,.0f}"
)

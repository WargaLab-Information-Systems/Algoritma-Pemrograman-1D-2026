belanja = int(input("Masukkan total belanja: Rp"))

print("Total belanja awal : Rp", belanja)

if belanja % 100000 == 0:
    bayar = 0
elif belanja % 50000 == 0:
    bayar = belanja * 50 // 100
elif belanja % 10000 == 0:
    bayar = belanja * 20 // 100
elif belanja >= 200000:
    bayar = belanja * 10 // 100
else:
    bayar = belanja

print("Total harga akhir : Rp", bayar)

# poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
# print("Status poin :", poin)

if bayar > 0:
    print("poin bertambah")
else:
    print("tidak ada point")

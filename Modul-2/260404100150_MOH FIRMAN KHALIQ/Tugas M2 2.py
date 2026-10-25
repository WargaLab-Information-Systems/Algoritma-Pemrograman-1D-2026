total_belanja = int(input("Masukkan total belanja: Rp"))


if total_belanja % 100000 == 0:
    total_bayar = 0
elif total_belanja % 50000 == 0:
    total_bayar = total_belanja * 50 // 100
elif total_belanja % 10000 == 0:
    total_bayar = total_belanja * 80 // 100
elif total_belanja >= 200000:
    total_bayar = total_belanja * 90 // 100
else:
    total_bayar = total_belanja


#poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"
if total_bayar > 0:
    poin = "Poin Bertambah"
else:
    poin = "Tidak bertambah"

print("HASIL BELANJA")
print("Total belanja awal : Rp", total_belanja)
print("Total harga akhir  : Rp", total_bayar)
print("Status Poin:", poin)
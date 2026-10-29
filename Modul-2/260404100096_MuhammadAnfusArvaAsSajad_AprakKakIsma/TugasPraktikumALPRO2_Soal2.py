totalBelanja = int(input("Masukkan total belanja: "))

print("Total belanja awal: Rp", totalBelanja)

if totalBelanja % 100000 == 0:
    totalBayar = 0
elif totalBelanja % 50000 == 0:
    totalBayar = totalBelanja * 0.5
elif totalBelanja % 10000 == 0:
    totalBayar = totalBelanja * 0.8
elif totalBelanja >= 200000:
    totalBayar = totalBelanja * 0.9
else:
    totalBayar = totalBelanja

print("Total harga akhir: Rp", totalBayar)

poin = "Poin Bertambah" if totalBayar > 0 else "Tidak Ada Poin"

print("Status poin:", poin)
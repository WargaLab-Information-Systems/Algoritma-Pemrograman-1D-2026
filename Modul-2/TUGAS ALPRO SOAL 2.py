total = int(input("Masukkan total belanja: Rp"))

if total % 100000 == 0:
    bayar = 0
elif total % 50000 == 0:
    bayar = total * 50 / 100
elif total % 10000 == 0:
    bayar = total * 20 / 100
elif total >= 200000:
    bayar = total * 10 / 100
else:
    bayar = total

print("Total belanja awal : Rp", total)
print("Total yang dibayar : Rp", bayar)

poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print("Status poin        :", poin) 
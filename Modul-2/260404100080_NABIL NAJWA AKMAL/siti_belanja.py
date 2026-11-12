total = int(input("Masukkan total belanja (Rp): "))

print("Total belanja awal:", total)

if total % 100000 == 0:
    bayar = 0
elif total % 50000 == 0:
    bayar = total // 2
elif total % 10000 == 0:
    bayar = total - total * 20 // 100
elif total >= 200000:
    bayar = total - total * 10 // 100
else:
    bayar = total

print("Total harga akhir:", bayar)

status = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print(status)

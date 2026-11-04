total = int(input("Masukkan total belanja: Rp"))

# menentukan diskon 
if total % 100000 == 0:
    diskon = 100 
elif total % 50000 == 0:
    diskon = 50
elif total % 10000 == 0:
    diskon = 20
elif  total >= 200000:
    diskon = 10
else:
    diskon = 0

# menghitung total akhir
total_diskon = total * diskon / 100
total_bayar = total - total_diskon

# menentukan poin operator menggunakan ternary operator
poin = "Poin Bertambah" if total_bayar > 0 else "tidak ada poin"

# menampilkan hasil
print("\n=== HASIL BELANJA ====")
print("Total belanja awal:", total)
print("Diskon :", diskon, "%")
print("Total yang dibayar :", total_bayar)
print("Status poin:", poin)
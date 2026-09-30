jumlah_buku = 3
harga_buku = 15000

jumlah_pulpen = 2
harga_pulpen = 5000

total_buku = jumlah_buku * harga_buku
total_pulpen = jumlah_pulpen * harga_pulpen

total_belanja = total_buku + total_pulpen

if total_belanja >= 50000:
    diskon = total_belanja * 10 / 100
else:
    diskon = 0

total_bayar = total_belanja - diskon

print("Total harga buku =", total_buku)
print("Total harga pulpen =", total_pulpen)
print("Total belanja sebelum diskon =", total_belanja)
print("Besarnya diskon =", diskon)
print("Total yang harus dibayar =", total_bayar)
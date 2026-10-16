# Program Kasir Supermarket KOPERASI NDESO

total_awal = int(input("Masukkan total belanja Siti (Rp): "))

# Cek diskon dari yang terbesar ke terkecil
if total_awal % 100000 == 0:
    diskon = 100
elif total_awal % 50000 == 0:
    diskon = 50
elif total_awal % 10000 == 0:
    diskon = 20
elif total_awal >= 200000:
    diskon = 10
else:
    diskon = 0

# Hitung potongan dan total akhir
potongan = total_awal * diskon / 100
total_akhir = total_awal - potongan

# Ternary operator untuk status poin 
if total_akhir > 0 :
    status_poin = "Ada Poin"
else : 
    status_poin = "Tidak Ada Poin"


# Tampilkan hasil
print("Total belanja awal :", total_awal)
print("Diskon             :", diskon, "%")
print("Total yang dibayar :", (total_akhir))
print("Status poin        :", status_poin)
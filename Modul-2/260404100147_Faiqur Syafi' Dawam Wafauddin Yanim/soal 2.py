total_awal = int(input("Masukkan total belanja Siti: Rp"))


if total_awal % 100000 == 0:
    total_akhir = 0
elif total_awal % 50000 == 0:
    total_akhir = total_awal - (total_awal * 0.50)
elif total_awal % 10000 == 0:
    total_akhir = total_awal - (total_awal * 0.20)
elif total_awal >= 200000:
    total_akhir = total_awal - (total_awal * 0.10)
else :
    total_akhir = total_awal

if total_akhir > 0 :
    status_poin = "Poin Bertambah"
else :
    status_poin = "Tidak ada Point"


status_poin = "Poin Bertambah 5" if total_akhir > 0 else "5"

if total_akhir > 0 :
    status_point = "Poin Bertambah"
else :
    status_point = "Tidak ada Point"

print("Total belanja awal: Rp", total_awal)
print("Total harga akhir: Rp ", (total_akhir))
print("Status Poin: ", status_poin)
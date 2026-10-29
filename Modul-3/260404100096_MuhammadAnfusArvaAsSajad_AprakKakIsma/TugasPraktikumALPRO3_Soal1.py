jumlahPenumpang = 0
totalPendapatan = 0
totalJarak = 0
jarakTerjauh = 0

print("=== KASIR TERMINAL BUS SIDOARJO ===")
print("Masukkan jarak penumpang (km), ketik 0 untuk berhenti")

while True:
    jarak = int(input("Jarak penumpang (km): "))

    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak tidak valid, silakan ulangi!")
        continue

    jumlahPenumpang += 1
    totalJarak += jarak

    if jarak > jarakTerjauh:
        jarakTerjauh = jarak

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if jumlahPenumpang % 5 == 0:
        tarif = tarif // 2
        print(f"Penumpang ke-{jumlahPenumpang} mendapat diskon 50%")

    print(f"Tarif penumpang ke-{jumlahPenumpang}: Rp{tarif:,}".replace(",", "."))
    totalPendapatan += tarif

print("\n=== REKAP AKHIR ===")
if jumlahPenumpang > 0:
    rataRata = totalJarak / jumlahPenumpang
    print("Jumlah penumpang :", jumlahPenumpang)
    print("Total pendapatan : Rp" + f"{totalPendapatan:,}".replace(",", "."))
    print("Jarak terjauh    :", jarakTerjauh, "km")
    print(f"Rata-rata jarak  : {rataRata:.2f} km")
else:
    print("Tidak ada penumpang yang dilayani.")
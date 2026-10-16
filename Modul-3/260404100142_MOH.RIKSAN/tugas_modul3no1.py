jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

print("=== Kasir Terminal Bus Sidoarjo ===")
while True:
    jarak = int(input("Masukkan jarak tempuh (km), 0 untuk selesai: "))

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid, ulangi!")
        continue

    jumlah_penumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Diskon 50% (penumpang ke- ", jumlah_penumpang)
        

    print(f"Tarif: Rp ", tarif )

    total_pendapatan += tarif
    total_jarak += jarak
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

print("\n=== Rekap ===")
if jumlah_penumpang == 0:
    print("Belum ada penumpang.")
else:
    print("Jumlah penumpang :", jumlah_penumpang)
    print(f"Total pendapatan : Rp{total_pendapatan:,.0f}")
    print("Jarak terjauh    :", jarak_terjauh, "km")
    print(f"Rata-rata jarak  : {total_jarak / jumlah_penumpang:.1f} km")
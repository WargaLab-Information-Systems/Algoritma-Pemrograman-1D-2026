jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

while True:
    jarak = int(input("Masukkan jarak penumpang (km, 0 untuk selesai): "))

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid, silakan ulangi!")
        continue

    jumlah_penumpang += 1
    total_jarak += jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000 * (jarak - 5)
    else:
        tarif = 13000 + 500 * (jarak - 15)

    if jumlah_penumpang % 5 == 0:
        tarif = tarif // 2
        print("Penumpang ke-", jumlah_penumpang, "mendapat diskon 50%")

    total_pendapatan += tarif
    print("Tarif penumpang ke-", jumlah_penumpang, ": Rp", tarif)

print("===== REKAP =====")
print("Jumlah penumpang :", jumlah_penumpang)
print("Total pendapatan : Rp", total_pendapatan)
print("Jarak terjauh    :", jarak_terjauh, "km")
print("Total Jarak      :", total_jarak, "km")

if jumlah_penumpang > 0:
    print("Rata-rata jarak  :", (total_jarak / jumlah_penumpang), "km")
else:
    print("Rata-rata jarak  : 0 km")
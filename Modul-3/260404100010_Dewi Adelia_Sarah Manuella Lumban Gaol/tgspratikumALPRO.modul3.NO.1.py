
jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    jarak = int(input("Masukkan jarak penumpang (km, 0 untuk selesai): "))

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid, masukkan ulang!")
        continue

    jumlah_penumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    # Diskon untuk penumpang ke-5, ke-10, dan seterusnya
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 50 // 100
        print("Mendapat diskon 50%")

    total_pendapatan += tarif
    total_jarak += jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    print("Tarif penumpang: Rp", tarif)

print("\n=== HASIL AKHIR ===")
print("Jumlah penumpang:", jumlah_penumpang)
print("Total pendapatan: Rp", total_pendapatan)

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
    print("Jarak terjauh:", jarak_terjauh, "km")
    print("Rata-rata jarak:", round(rata_rata, 2), "km")
else:
    print("Belum ada penumpang yang dihitung.")

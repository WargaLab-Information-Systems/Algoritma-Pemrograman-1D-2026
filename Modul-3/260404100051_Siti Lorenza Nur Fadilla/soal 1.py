jumlah = total = terjauh = total_jarak = 0

while True:
    jarak = float(input("Jarak (km, 0 = selesai): "))
    if jarak == 0:
        break
    if jarak < 0:
        print("Tidak valid, ulangi!")
        continue

    jumlah += 1
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000 * (jarak - 5)
    else:
        tarif = 13000 + 500 * (jarak - 15)

    if jumlah % 5 == 0:     
        tarif = tarif / 2

    print("Tarif: Rp", int(tarif))
    total += tarif
    total_jarak += jarak
    if jarak > terjauh:
        terjauh = jarak

print("Jumlah penumpang:", jumlah)
print("Total pendapatan: Rp", int(total))
print("Jarak terjauh:", terjauh, "km")
if jumlah > 0:
    print("Rata-rata jarak:", round(total_jarak / jumlah, 2), "km")
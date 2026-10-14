def hitung_tarif(jarak):
    if jarak <= 5:
        return 3000
    elif jarak <= 15:
        return 3000 + 1000 * (jarak - 5)
    else:
        return 13000 + 500 * (jarak - 15)


jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    try:
        jarak = int(input("Masukkan jarak (km), 0 untuk selesai: "))
    except ValueError:
        print("Input harus bilangan angka bulat.")
        continue

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid, harus diulangi.")
        continue

    jumlah_penumpang += 1
    tarif = hitung_tarif(jarak)

    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print(f"Penumpang ke-{jumlah_penumpang} diskon 50%: Rp{tarif:,.0f}")
    else:
        print(f"Penumpang ke-{jumlah_penumpang}: Rp{tarif:,.0f}")

    total_pendapatan += tarif
    total_jarak += jarak
    jarak_terjauh = max(jarak_terjauh, jarak)
    
print("\n=== Rekap data yang didapat ===")
print(f"Jumlah penumpang : {jumlah_penumpang}")
print(f"Total pendapatan : Rp{total_pendapatan:,.0f}")
if jumlah_penumpang > 0:
    print(f"Jarak terjauh    : {jarak_terjauh} km")
    print(f"Rata-rata jarak  : {total_jarak / jumlah_penumpang:.2f} km")
else:
    print("Jarak terjauh    : -")
    print("Rata-rata jarak  : -")
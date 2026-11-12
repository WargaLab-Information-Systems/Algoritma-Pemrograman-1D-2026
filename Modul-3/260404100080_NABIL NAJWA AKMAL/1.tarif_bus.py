jarak = int(input("Masukkan jarak penumpang (0 untuk berhenti): "))

jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

while jarak != 0:
    if jarak < 0:
        print("Jarak tidak valid, silakan ulangi")
        jarak = int(input("Masukkan jarak penumpang (0 untuk berhenti): "))
    else:
        jumlah_penumpang = jumlah_penumpang + 1
        total_jarak = total_jarak + jarak

        if jarak > jarak_terjauh:
            jarak_terjauh = jarak

        if jarak <= 5:
            tarif = 3000
            print(tarif)
        elif jarak <= 15:
            tarif = 3000 + (jarak - 5) * 1000
            print(tarif)
        else:
            tarif = 13000 + (jarak - 15) * 500
            print(tarif)

        if jumlah_penumpang % 5 == 0:
            tarif = tarif / 2
            print(tarif)
            print("Penumpang ke-", jumlah_penumpang, "dapat diskon 50%")

        total_pendapatan = total_pendapatan + tarif
        jarak = int(input("Masukkan jarak penumpang (0 untuk berhenti): "))

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
else:
    rata_rata = 0

print("Jumlah penumpang:", jumlah_penumpang)
print("Total pendapatan: Rp", total_pendapatan)
print("Jarak terjauh:", jarak_terjauh, "km")
print("Rata-rata jarak:", rata_rata, "km")

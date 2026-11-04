jumlahPenumpang = 0
totalPendapatan = 0
jarakTerjauh = 0
totalJarak = 0

while True:
    jarak = int(input("Masukkan jarak (KM): "))

    if jarak == 0:
        break
    elif jarak < 0: 
        continue

    jumlahPenumpang += 1
    totalJarak += jarak

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (1000 *(jarak - 5))
    else:
        tarif = 13000  + (500 * (jarak - 15))

    if jumlahPenumpang % 5 == 0:
        tarif = tarif * (50/100)

    totalPendapatan += tarif

    if jarak > jarakTerjauh:
        jarakTerjauh = jarak

print ("Jumlah penumpang:", jumlahPenumpang)
print ("Total pendapatan:", totalPendapatan)
print ("Jarak terjauh:", jarakTerjauh)
print ("Rata-rata jarak:", totalJarak / jumlahPenumpang)
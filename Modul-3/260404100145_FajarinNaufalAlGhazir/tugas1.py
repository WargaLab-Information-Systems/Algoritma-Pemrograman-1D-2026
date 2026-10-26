jumlahPenumpang = 0
totalPendapatan = 0
jarakTerjauh = 0
totalJarak = 0

while True:
    jarak = int(input("Masukkan jarak penumpang (km): "))

    if jarak < 0:
        continue
    if jarak == 0:
        sistem = False
        break
    else:
        sistem = True

    if jarak <= 5:
        tarif = 3000
    elif jarak >= 6 and jarak <= 15:
        tarif = 3000 + (1000 *(jarak - 5))
    else:
        tarif = 13000 + (500 *(jarak - 15))

    jumlahPenumpang += 1
    if jumlahPenumpang % 5 == 0:
        tarif = tarif * (50/100)

    totalPendapatan += tarif
    totalJarak += jarak
    if jarak > jarakTerjauh:
        jarakTerjauh = jarak

if sistem == False and jumlahPenumpang == 0:
    print(f"Program selesai.")
    exit()

rataRataJarak = totalJarak / jumlahPenumpang

# print("-" * 35)
print(f"-" * 35)
print(f"Jumlah penumpang    : {jumlahPenumpang}")
print(f"Total pendapatan    : Rp{int(totalPendapatan)}")
print(f"Jarak terjauh       : {jarakTerjauh}km")
print(f"Rata rata jarak     : {int(rataRataJarak)}km")
print("-" * 35)
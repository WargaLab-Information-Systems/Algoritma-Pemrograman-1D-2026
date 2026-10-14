jarak = int(input("berapa jarak yang di tempuh: "))
penumpang = 0
pendapatan = 0
jarak_jauh = 0
total_jarak = 0

while jarak !=0:
    if jarak < 0:
        print("jarak tidak valid")
        jarak = int(input("berapa jarak yang di tempuh: "))
        continue

    penumpang +=1

    total_jarak += jarak
    if jarak > jarak_jauh:
        jarak_jauh = jarak

    if jarak <=5:
        tarif = 3000
    elif jarak >5 and jarak <=15:
        tarif = (jarak - 5) * 1000 + 3000
    elif jarak > 15:
        tarif = (jarak - 15) * 500 + 13000
    else:
        print("jarak tidak dapat di proses")
    
    if penumpang %5 == 0:
        diskon = tarif * 50//100
    else:
        diskon = 0
    
    bayar = tarif - diskon
    pendapatan += bayar
    print ("tarif: ", tarif)
    jarak = int(input("berapa jarak yg di tempuh: "))

print (" jumlah penumpang:", penumpang)
print ("jarak terjauh:", jarak_jauh)
print("jumlah pendapatan:", pendapatan)

if penumpang > 0:
    rata_rata = total_jarak / penumpang
    print("rata-rata jarak: ", rata_rata)
else:
    print("tidak ada penumpang hari ini")
    
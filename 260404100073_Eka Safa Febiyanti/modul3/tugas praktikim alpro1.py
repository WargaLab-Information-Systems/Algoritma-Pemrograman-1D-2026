jumlah = 0
total = 0 
terjauh = 0
total_jarak = 0

while True:
    jarak = int(input("masukkan jarak (km): "))

    if jarak == 0:
        break
    if jarak < 0:
        print ("jarak tidak valid, ulangi!")
        continue
    jumlah += 1
    total_jarak += jarak

    if jarak <= 5:
        tarif = 3000
        print("tarif :",tarif)
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
        print("tarif :",tarif)
    else:
        tarif = 13000 +(jarak - 15) * 500
        print("tarif :",tarif)

    if jumlah % 5 == 0:
        tarif = tarif * 0.5
        print ("mendapat diskon 50%")

    total += tarif

    if jarak > terjauh:
        terjauh = jarak
        
print("tarif: Rp", tarif)
print("jumlah penumpang:", jumlah)
print("total pendapatan: Rp", total)
print("jarak terjauh:", terjauh, "km")

if jumlah > 0:
    rata = total_jarak / jumlah 
    print("rata-rata jarak:", rata, "km")
else:
    print("rata-rata jarak: 0 km")
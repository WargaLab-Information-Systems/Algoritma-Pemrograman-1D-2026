# Inisialisasi variabel
jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
ratarata_jarak = 0
total_jarak = 0

# input jarak penumpang
while True:
    jarak = float(input("memasukkan jarak: "))
    
    if jarak == 0:
        break
    elif jarak < 0:
        print("jarak negatif dianggap tidak valid dan harus diulang")
        continue # melewati sisa proses untuk potaran ini, dan kembali meminta input jarak
    # ngitung tarif berdasarkan jarak
    elif jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5 ) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500
        
    # ngitung jumlah penumpang valid
    jumlah_penumpang += 1
    
    # ngitung diskon 50%
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 50/100
        print("Penumpang mendapat diskon 50%")
        
    # ngakumulasi pendapatan dan jarak
    total_pendapatan += tarif
    total_jarak += jarak
    
    print("Tarif penumpang:", tarif)
    
     # cari jarak terjauh
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak
        
if jumlah_penumpang > 0:
        ratarata_jarak = total_jarak / jumlah_penumpang
        
        print("=== HASIL AKHIR ===")
        print("Jumlah penumpang:", jumlah_penumpang)
        print("Total pendapatan:", total_pendapatan)
        print("Jarak terjauh:", jarak_terjauh, "km")
        print("Rata-rata jarak:", ratarata_jarak, "km")
else:
        print("Belum ada penumpang.")
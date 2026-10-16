# ini adalahinput untuk 3 jenis tiket pada inputan harus memsaukkann variable tiket
reguler1 = 40000
vip1= 75000
vvip1 = 100000
pelanggan = input("Masukkan jenis tiket pelanggan: ")
jenis_tiket = 0
# pelanggan bisa membeli lebih dari satu tiket dan bisa membeli lebiih dari satu tiket yang sama
while True:
    if pelanggan == reguler1:
        break
    if pelanggan == vip1:
        break
    if pelanggan == vvip1:
        break
    if pelanggan == 0:
        continue

jenis_tiket = jenis_tiket + 1
# code ini untuk menentukan apakah user membeli minum atau tidak dan jika membeli minum 1 atau lebih maka akan mendapatkan harga 10000 dan jika kurang dari 1 akan 0
if reguler1 > 1:
    print("membeli tiket reguler: ")
    minuman = "y/Y"
    minuman = input("jumlah minuman: ")
    if minuman > 1:
        harga = 10000
    else:
        harga = 0 
# khusus tiket vip dan vvip pelanggan mendapatkan minum gratis dan makanan gratis 
if vip1 == 1:
    print("mendapatkan makanan dan minuman gratis: ")
if vvip1 == 1:
    print("mendapatkan makanan dan minuman gratis: ")

# menghitung diskon jika tiket yang dibeli lebih dari 3 dan jika pelanggan mempunyai member card mendapatkan diskon 10%
# jika pelanggan tidak memiliki member card maka tidak mendapatkan diskon
jumlah_tiket = input("masukkan jumlah tiket: ")
if jumlah_tiket > 3:
    diskon = jumlah_tiket * 0.1
    print("mendapatkan diskon 10%")
else:
    print("tidak mendapatkan diskon: ")

# perulangan untuk sistem pembayaran program akan terus meminta nominal uang
pembayaran = 0
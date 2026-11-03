regular = 0
jumlahRegular = 0
vip = 0
jumlahVip = 0
vvip = 0
jumlahVvip = 0
jumlahTiket = 0
minuman = 0
minumGratis = False
member = False
hargaRegular = 40000
hargaVip = 75000
hargaVvip = 100000
hargaMinum = 10000

#Value di atas agar saat print tidak terjadi error

while True:
    print("---" * 20)
    pilihTiket = input("Pilih tiket anda \na. Regular\nb. VIP\nc. VVIP\n(Cukup masukkan a/b/c)\nMasukkan angka 0 jika selesai memesan\n: ")
    if pilihTiket == "0":
        break
    pilihJumlah = int(input("Masukkan jumlah tiket anda: "))
    print("---" * 20)
    
    if pilihTiket == "a":
        regular += 1
        jumlahRegular += pilihJumlah
        jumlahTiket += pilihJumlah
        print("---" * 20)
        tambahMinum = input("Apakah anda ingin menambah pesanan minuman? (Y/N) ")
        print("---" * 20)
        if tambahMinum == "Y" or tambahMinum =="y":
            minuman += 1
    elif pilihTiket == "b":
        vip += 1
        jumlahVip += pilihJumlah
        jumlahTiket += pilihJumlah
        minumGratis = True
        print("---" * 20)
        print("Anda mendapatkan minuman gratis")
        print("---" * 20)
    elif pilihTiket == "c":
        vvip += 1
        jumlahVvip += pilihJumlah
        jumlahTiket += pilihJumlah
        minumGratis = True
        print("---" * 20)
        print("Anda mendapatkan minuman gratis")
        print("---" * 20)
    else:
        print("---" * 20)
        print("Masukkan nilai yang benar")
        print("---" * 20)
        continue

print("---" * 20)
member = input("Apakah anda mempunyai kartu member? (Y/N)")
print("---" * 20)
if member == "Y" or member == "y":
    member = True

if jumlahTiket > 3:
    if member == True:
        diskon = 15/100
    else:
        diskon = 10/100
        
if minumGratis == True:
    minuman = 0

totalHarga = (hargaRegular * jumlahRegular) + (hargaVip * jumlahVip) + (hargaVvip * jumlahVvip) + (hargaMinum * minuman)

if member == True:
    totalHarga = totalHarga * diskon
else:
    pass

print("---" * 20)
print(f"Total harga Rp{totalHarga}")
print("---" * 20)

while True:
    print("---" * 20)
    bayar = int(input("Bayar: "))
    print("---" * 20)
    if bayar >= totalHarga:
        print("---" * 20)
        print("Terimakasih atas pesanannya :)")
        if bayar > totalHarga:
            kembalian = bayar - totalHarga
            print(f"Kembalian anda Rp{kembalian}")
            print("---" * 20)
        break
    else:
        print("---" * 20)
        print("Uang anda kurang :)")
        print("---" * 20)
        continue
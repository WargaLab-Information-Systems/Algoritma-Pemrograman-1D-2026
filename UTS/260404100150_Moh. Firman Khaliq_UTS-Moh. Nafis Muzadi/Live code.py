regular
vip
vvip

#INPUTAN UNTUK MEMBELI TIKET DAN MEMILIH JUMLAH TIKET
while True:
    tiket_dibeli = input("Masukkan tiket yang dibeli: ")
    jumlah_tiket = input("Masukkan jumlah tiket: ")
    member_card = input("Apakah anda punya member card (Ya/tidak)")

#PERHITUNGAN HARGA TIKET
if tiket_dibeli = regular:
    harga = 40000 * jumlah_tiket
elif tiket_dibeli = vip:
    harga = 75000 * jumlah_tiket
elif tiket_dibeli = vvip:
    harga = 100000 * jumlah_tiket
else:
    print("Tiket Tidak valid")


if tiket_dibeli == regular:
    print("anda bisa membeli minuman seharga 10000 Ribu Rupiah")
    minuman = input("beli atau tidak (Y/N)")
    if minuman == Y:
        harga += 10000
    else minuman == N:
        continue
    
if member_card ==  Ya:
    if jumlah_tiket > 3:
        harga_total = harga * 0.15
        if  member_card == Tidak:
            if  jumlah_tiket > 3:
                harga_total = harga * 0.1

nominal = input("Masukkan jumlah uang")
kembalian = nominal -  harga Total


print(f"Harga total: {harga_total} Rp.")
if tiket_dibeli == vip or vvip:
    print("Anda Mendapat Minuman Gratis")
print(f"nominal{nomimal}")
print(f"kembalian{kembalian}")


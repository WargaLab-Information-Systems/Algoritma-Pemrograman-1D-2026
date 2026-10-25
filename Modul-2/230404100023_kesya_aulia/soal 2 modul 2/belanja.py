
total_awal = int(input("Masukkan total belanja :"))

total_belanja = print("total belanja :", total_awal)

if total_awal % 100000 == 0:
    bayar = 0
elif total_awal % 50000 == 0:
    bayar = total_awal * 50/100
elif total_awal % 10000 == 0:
    bayar = total_awal * 20/100
elif total_awal >=200000:
    bayar = total_awal * 10/100
else:
    bayar = total_awal 

total_akhir = print("total belanja anda setelah mendapatkan diskon adalah :", bayar)

if bayar >0 :
    print("point bertambah")
else:
    print("tidak ada point")


# cetak_point = "point bertambah" if bayar > 0 else "Tidak ada point"
# print(cetak_point)
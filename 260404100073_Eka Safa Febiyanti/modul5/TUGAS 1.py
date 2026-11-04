def jumlah_pelanggan(n):
    if n == 1 or n == 2:
        return 1
    else:
        return jumlah_pelanggan(n-1) + jumlah_pelanggan(n-2)

hari = int(input("Masukkan hari ke-N: "))

hasil = jumlah_pelanggan(hari)

print("Jumlah pelanggan pada hari ke-", hari, "adalah", hasil)
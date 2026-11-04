def hitung_pelanggan(n):
    if n == 1 or n == 2:
        return 1
    else:
        return hitung_pelanggan(n - 1) + hitung_pelanggan(n - 2)


hari = int(input("Masukkan hari ke-N: "))
jumlah = hitung_pelanggan(hari)
print(f"Jumlah pelanggan pada hari ke-{hari} adalah {jumlah} orang.")
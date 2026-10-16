while True:
    n = int(input("Masukkan tinggi setengah menara (2-15): "))
    if 2 <= n <= 15:
        break
    print("Tidak valid, masukkan angka 2 sampai 15!")

# bagian atas membesar sampai n, lalu mengecil kembali
urutan_baris = list(range(1, n + 1)) + list(range(n - 1, 0, -1))

for i in urutan_baris:
    baris = ""
    for k in range(1, i + 1):        # naik 1 sampai i
        baris += str(k % 10)         # angka terakhirnya saja
    for k in range(i - 1, 0, -1):    # turun kembali ke 1
        baris += str(k % 10)
    print(" " * (n - i) + baris)     # spasi di depan agar rata tengah
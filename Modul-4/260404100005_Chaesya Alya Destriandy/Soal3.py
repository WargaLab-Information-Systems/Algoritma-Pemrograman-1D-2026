n = int(input("Masukkan bilangan bulat positif: "))

for i in range(1, n + 1): # ngitung banya baris
    # cetak angka piramid kiri, dari kecil ke besar
    for j in range(1, i + 1):
        print(j, end="")

    # cetak spasi diantara dua piramid
    for j in range(2 * (n - i) + 1):
        print(" ", end="")

    # cetak piramid kanan cetak angka dari besar ke kecil
    for j in range(i, 0, -1):
        print(j, end="")

    print()






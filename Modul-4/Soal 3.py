n = int(input("Masukkan bilangan bulat positif: "))

for baris in range(1, n + 1):
    # spasi kiri agar piramida kiri rata kanan
    for spasi in range(n - baris):
        print(" ", end=" ")

    for angka in range(1, baris + 1):
        print(angka, end=" ")

    for spasi in range(n):
        print(" ", end="")

    for angka in range(baris, 0, -1):
        print(angka, end=" ")

    print()
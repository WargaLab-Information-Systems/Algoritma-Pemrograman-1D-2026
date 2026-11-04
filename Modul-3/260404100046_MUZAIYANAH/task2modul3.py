n = 0

while n < 2 or n > 15:
    n = int(input("Masukkan tinggi setengah menara (2 - 15): "))
    print("Tinggi setengah menara tidak valid, harus diantara 2 hingga 15!")

for baris in range(1, n + 1):
    spasi = (n - baris) * 2
    hasil = ""

    for angka in range(1, baris + 1):
        hasil = hasil + str(angka % 10) + " "
    for angka in range(baris - 1, 0, -1):
        hasil = hasil + str(angka % 10) + " "

    print(" " * spasi + hasil)

for baris in range(n - 1, 0, -1):
    spasi = (n - baris) * 2
    hasil = ""

    for angka in range(1, baris + 1):
        hasil = hasil + str(angka % 10) + " "
    for angka in range(baris - 1, 0, -1):
        hasil = hasil + str(angka % 10) + " "

    print(" " * spasi + hasil)






# baris = n - 1
# while baris >= 1:
#     space = (n - baris) * 2
#     hasil = ""

#     for angka in range(1, baris + 1):
#         hasil = hasil + str(angka % 10) + " "
#     for angka in range(baris - 1, 0, -1):
#         hasil = hasil + str(angka % 10) + " "

#     print(" " * space + hasil)
#     baris -= 1
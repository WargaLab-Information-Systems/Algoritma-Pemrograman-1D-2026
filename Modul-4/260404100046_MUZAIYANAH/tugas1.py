# jumlahBaris = int(input("Masukkan jumlah baris: "))
# jumlahLampu = int(input("Masukkan jumlah lampu: "))

# nomorLampu = 1

# for baris in range (1,jumlahBaris+1):
#     print("Baris", baris)
#     for lampu in range (1, jumlahLampu+1):
#         if nomorLampu % 3 == 0:
#             print(" Lampu ke", nomorLampu, "mengalami gangguan")
#         else:
#             print(" Lampu ke", nomorLampu, "berfungsi normal!")
#         nomorLampu +=1

# print("Silahkan periksa sumber listrik utama taman!")





jumlahBaris = int(input("Masukkan jumlah baris: "))
jumlahLampu = int(input("Masukkan jumlah lampu: "))

for baris in range (1,jumlahBaris + 1):
    print("Baris", baris)
    for lampu in range (1, jumlahLampu + 1):
        if lampu % 3 == 0:
            print(" Lampu ke", lampu, "mengalami gangguan!")
        elif lampu %2 == 0:
            print(" Lampu ke", lampu, "mengalami error!")
        else:
            print(" Lampu ke", lampu, "berfungsi normal")

print("Silahkan periksa sumber listrik utama taman!")
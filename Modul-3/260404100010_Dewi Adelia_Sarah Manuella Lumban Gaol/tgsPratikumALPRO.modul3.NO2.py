
while True:
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

    if n >= 2 and n <= 15:
        break
    else:
        print("Input salah! Masukkan angka 2 sampai 15.")

# Bagian atas menara
for i in range(1, n + 1):
    # Membuat spasi agar rata tengah
    print(" " * (n - i), end="")

    # bagian kanan
    for j in range(1, i + 1):
        print(j % 10, end="")

    # Angka turun
    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()

# Bagian kiri
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()
    

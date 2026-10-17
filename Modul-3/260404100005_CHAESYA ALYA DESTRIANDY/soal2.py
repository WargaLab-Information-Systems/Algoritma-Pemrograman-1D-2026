while True:
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

    if n >= 2 and n <= 15:
        break

    print("Input tidak valid! Masukkan angka 2 sampai 15.")

# Bagian atas: membesar
for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()

# Bagian bawah: mengecil
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()

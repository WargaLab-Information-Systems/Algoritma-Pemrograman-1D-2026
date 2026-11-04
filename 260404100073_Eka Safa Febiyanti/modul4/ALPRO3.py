n = int(input("Masukkan jumlah baris: "))

for i in range(1, n + 1):
    # Piramida pertama
    for j in range(1, i + 1):
        print(j, end="")

    # Memberikan jarak
    print(" " * (2 * (n - i)), end="")

    # Piramida kedua (cermin)
    for j in range(i, 0, -1):
        print(j, end="")

    print()
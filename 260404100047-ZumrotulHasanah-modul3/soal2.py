n = int(input("Masukkan tinggi menara (2-15): "))

if n < 2 or n > 15:
    print("Tinggi harus antara 2 sampai 15!")
else:
    for i in range(1, n + 1):
        baris = " " * (n - i)

        for j in range(1, i + 1):
            baris += str(j % 10)

        for j in range(i - 1, 0, -1):
            baris += str(j % 10)

        print(baris)

    for i in range(n - 1, 0, -1):
        baris = " " * (n - i)

        for j in range(1, i + 1):
            baris += str(j % 10)

        for j in range(i - 1, 0, -1):
            baris += str(j % 10)

        print(baris)
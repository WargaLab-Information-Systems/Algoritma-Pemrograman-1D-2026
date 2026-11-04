n = int(input("Masukkan tinggi setengah menara (2-15): "))
while n < 2 or n > 15:
    print("Input tidak valid, ulangi!")
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

lebar = 2 * n - 1


for i in range(1, n + 1):
    baris = ""
    for j in range(1, i + 1):
        baris += str(j % 10)
    for j in range(i - 1, 0, -1):
        baris += str(j % 10)
    print(baris.center(lebar))


for i in range(n - 1, 0, -1):
    baris = ""
    for j in range(1, i + 1):
        baris += str(j % 10)
    for j in range(i - 1, 0, -1):
        baris += str(j % 10)
    print(baris.center(lebar))
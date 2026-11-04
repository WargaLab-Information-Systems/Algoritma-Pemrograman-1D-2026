while True:
    n = int(input("masukkan tinggi menara (2-15): "))
    if 2 <= n <= 15:
        break
    print("tinggi tidak valid, ulangi")

for i in range(1, 2 * n):

    if i <= n:
        baris = i
    else:
        baris = 2 * n - i

    pola = ""


    for j in range(1, baris + 1):
        pola += str(j % 10)

    for j in range(baris - 1, 0, - 1):
        pola += str(j % 10)

    print(pola.center(2 * n - 1))
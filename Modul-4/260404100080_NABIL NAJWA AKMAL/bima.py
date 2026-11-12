n = int(input("Masukkan nilai yg ingin anda masukkan: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print(" " * ((n - i) * 4), end=" ")

    for k in range(i, 0, -1):
        print(k, end=" ")
    print()
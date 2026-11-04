n = int(input("Masukkan bilangan bulat positif: "))

if n > 0:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")

        for j in range(1, 2 * (n - i) + 2):
            print(" ", end=" ")

        for j in range(i, 0, -1):
            print(j, end=" ")

        print()
else:
    print("Masukkan bilangan bulat positif!")

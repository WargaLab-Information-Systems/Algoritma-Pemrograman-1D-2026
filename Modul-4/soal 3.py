
n = int(input("Masukkan n: "))

for i in range(1, n + 1):

    for k in range(1, i + 1):
        print(k, end='')

    for j in range(n - i):
        print(' ', end=' ')

    for k in range(i, 0, -1):
        print(k, end='')

    print()

    

n = int(input("Masukkan tinggi setengah menara (2 - 15): "))

while n < 2 or n > 15:
    print("Tidak valid, silakan ulangi")
    n = int(input("Masukkan tinggi setengah menara (2 - 15): "))

i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end="")
        j = j + 1
    j = 1
    while j <= i:
        print(j % 10, end="")
        j = j + 1
    j = i - 1
    while j >= 1:
        print(j % 10, end="")
        j = j - 1
    print("")
    i = i + 1

i = n - 1
while i >= 1:
    j = 1
    while j <= n - i:
        print(" ", end="")
        j = j + 1
    j = 1
    while j <= i:
        print(j % 10, end="")
        j = j + 1
    j = i - 1
    while j >= 1:
        print(j % 10, end="")
        j = j - 1
    print("")
    i = i - 1

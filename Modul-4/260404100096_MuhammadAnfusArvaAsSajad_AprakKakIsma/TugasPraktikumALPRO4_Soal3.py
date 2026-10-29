n = int(input("Masukkan n (bilangan bulat positif): "))
while n <= 0:
    print("Input tidak valid, n harus bilangan bulat positif!")
    n = int(input("Masukkan n (bilangan bulat positif): "))

lebar = len(str(n)) + 1
jarak = 4

print()
for baris in range(1, n + 1):
    for angka in range(1, baris + 1):
        print(str(angka).ljust(lebar), end="")

    print(" " * (2 * (n - baris) * lebar + jarak), end="")

    for angka in range(baris, 0, -1):
        print(str(angka).rjust(lebar), end="")

    print()
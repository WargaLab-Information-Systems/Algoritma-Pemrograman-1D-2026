print("=== MENARA LAMPU HIAS ===")
n = int(input("Masukkan tinggi setengah menara (2-15): "))

while n < 2 or n > 15:
    print("Input tidak valid, harus antara 2 sampai 15!")
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

print()
for baris in range(1, 2 * n):
    if baris <= n:
        i = baris
    else:
        i = 2 * n - baris

    print(" " * (n - i), end="")

    for angka in range(1, i + 1):
        print(angka % 10, end="")

    for angka in range(i - 1, 0, -1):
        print(angka % 10, end="")

    print()
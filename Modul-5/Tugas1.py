# n = int(input("Masukkan hari ke-N: "))

# a, b = 1, 1
# for i in range(3, n + 1):
#     a, b = b, a + b

# print(f"Jumlah pelanggan pada hari ke-{n}: {b} orang")

def pelanggan(n):
    if n <= 2:
        return 1
    return pelanggan(n - 1) + pelanggan(n - 2)

n = int(input("masukkan hari: "))
print(f"Jumlah pelanggan pada hari ke-{n}: {pelanggan(n)} orang")
n = int(input("Masukkan hari ke: "))

def pelanggan(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return pelanggan(n - 2) + pelanggan(n - 1)
    else:
        print("masukkan angka yg benar")

print(pelanggan(n))
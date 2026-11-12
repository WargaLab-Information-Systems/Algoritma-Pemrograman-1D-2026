def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Masukkan hari ke-N (bilangan bulat positif): "))
while n <= 0:
    print("Input tidak valid, N harus bilangan bulat positif!")
    n = int(input("Masukkan hari ke-N (bilangan bulat positif): "))

jumlahPelanggan = fibonacci(n)
print(f"Jumlah pelanggan pada hari ke-{n}: {jumlahPelanggan} orang")
print(f"Jumlah pelanggan pada hari ke-{n}: {fibonacci(n)} orang")
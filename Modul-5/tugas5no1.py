def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


hari = int(input("Masukkan hari ke-: "))

while hari <= 0:
    print("Masukkan bilangan positif!")
    hari = int(input("Masukkan hari ke-: "))

print("Jumlah pelanggan pada hari ke-", hari, "adalah:", fibonacci(hari))
hari = int(input("Masukkan hari ke-: "))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if hari > 0:
    print("Jumlah pelanggan hari ke-", hari, "adalah", fibonacci(hari))
else:
    print("Hari harus berupa bilangan bulat positif!")







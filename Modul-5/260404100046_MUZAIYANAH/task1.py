# def pelanggan(n):
#     if n <= 2:
#         return 1
#     return pelanggan(n - 1) + pelanggan(n - 2)
 
 
# N = int(input("Masukkan hari ke-N: "))
# print("Jumlah pelanggan pada hari ke-" + str(N) + "adalah" + str(pelanggan(N)) + "orang")










def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


    print("Pelanggan pada hari ke-", n, "=", fibonacci(n))
n = int(input("Masukkan hari : "))

if n < 0:
    print("Masukkan bilangan positif!")
else:
    print("Pelanggan pada hari ke-", n, "=", fibonacci(n))
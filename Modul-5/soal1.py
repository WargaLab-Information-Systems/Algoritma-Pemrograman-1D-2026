def pelanggan(n): 
    if n == 1 or n == 2: 
        return 1
    else:
        return pelanggan(n - 1) + pelanggan(n - 2) 
 
N = int(input("Masukkan hari ke-N : "))
if N < 0 :
    print("harus bilangan bulat positif")
else:
    print("Jumlah pelanggan pada hari ke", N, "adalah", pelanggan(N))
    
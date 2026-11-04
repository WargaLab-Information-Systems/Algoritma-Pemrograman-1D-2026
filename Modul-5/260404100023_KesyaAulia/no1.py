hari = int(input("hari ke: "))
if hari <=0:
    print("masukkan hari yang benar")

def fibonacci(hari):
    if hari == 1 or hari == 2:   
        return 1
    else:
        return fibonacci(hari-1) + fibonacci(hari-2)

if hari > 0:
    print("pada hari ke", hari, "jumlah pelanggan", fibonacci(hari))
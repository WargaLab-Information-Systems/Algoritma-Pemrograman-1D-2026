penerima_penuh = 0

for i in range(1, 11):
    nama = input("masukkan nama: ")
    ipk = float(input("masukkan ipk: "))

    if ipk <3.00:
        print("tidak memenuhi syarat")
        continue
    
    penghasilan = int(input("masukkan penghasilan orang tua"))

    if penghasilan <= 3000000:
        print("mendapat beasiswa penuh")
        penerima_penuh += 1
    elif penghasilan <=5000000:
        print("mendapat beasiswa sebagian")
    else:
        print("tidak mendapat beasiswa")

    if penerima_penuh == 3:
        break
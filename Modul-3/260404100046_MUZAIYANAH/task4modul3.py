beasiswaPenuh = 0
for i in range(1, 11):
    print("Mahasiswa ke-",i)
    nama = input("Masukkan Nama: ")
    ipk = float(input("Masukkan IPK: "))
    penghasilan = int(input("Masukkan penghasilan orang tua perbulan: "))
                                   
    if ipk < 3.0:
        print(nama, "tidak memenuhi syarat.")
        continue
    
    if penghasilan <= 3000000:
        print(nama, "mendapatkan beasiswa penuh")
        beasiswaPenuh += 1
        if beasiswaPenuh == 3:
            print("Kuota beasiswa penuh.")
            break
    elif penghasilan > 3000000 and penghasilan <= 5000000:
        print(nama, "mendapatkan beasiswa sebagian")
    else:
        print(nama, "tidak mendapatkan beasiswa.")
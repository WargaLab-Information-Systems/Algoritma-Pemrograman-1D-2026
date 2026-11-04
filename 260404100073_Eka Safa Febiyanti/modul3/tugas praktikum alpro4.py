# Variable awal 
penuh = 0 

# Perulangan maksimal 10 mahasiswa 
for i in range (1, 11 ) :
    print ("/nMahasiswa ke-",i)

    nama = input ("Masukkan nama :")
    ipk = float(input("Masukkan IPK:"))

    # Memeriksa IPK 
    if ipk < 3.00:
        print (nama,": Tidak memenuhi")
        continue
    penghasilan = int(input("masukkan hasil orang tua per bulan: "))
        
    #Memasukkan hasil seleksi 
    if penghasilan <= 3000000:
        print (nama,": Beasiswa Penuh")
        penuh += 1

    elif penghasilan <= 5000000:
        print (nama,": Beasiswa  sebagian")
    else:
        print (nama,":Tidak mendapat beasiswa")

    #Memeriksa kuota beasiswa penuh
    if penuh == 3:
        print ("/nKuota beasiswa penuh sudah terpenuhi!")
        print("proses seleksi dihentikan")
        break


print ("/n===SELEKSI SELESAI ===")
print("Jumlah penerima beasiswa penuh:", penuh)
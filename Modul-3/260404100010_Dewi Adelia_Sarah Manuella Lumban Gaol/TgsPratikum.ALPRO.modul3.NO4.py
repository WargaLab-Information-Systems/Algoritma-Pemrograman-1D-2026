
jumlah_penuh = 0

for i in range(1, 11):
    print("\nMahasiswa ke-", i)

    nama = input("Masukkan nama: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print("Nama:", nama)
        print("Tidak memenuhi syarat beasiswa.")
        continue

    penghasilan = int(input("Masukkan penghasilan orang tua per bulan: "))

    if penghasilan <= 3000000:
        status = "Beasiswa penuh"
        jumlah_penuh += 1
    elif penghasilan <= 5000000:
        status = "Beasiswa sebagian"
    else:
        status = "Tidak mendapatkan beasiswa"

    print("Nama:", nama)
    print("IPK:", ipk)
    print("Penghasilan orang tua: Rp", penghasilan)
    print("Hasil seleksi:", status)

    if jumlah_penuh == 3:
        print("\nKuota beasiswa penuh sudah terpenuhi.")
        print("Proses seleksi dihentikan.")
        break

print("\nJumlah penerima beasiswa penuh:", jumlah_penuh)
jumlah_penuh = 0

for i in range(10):
    if jumlah_penuh == 3:
        print("\nKuota beasiswa penuh sudah terpenuhi.")
        break

    print("\nMahasiswa ke-", i + 1)

    nama = input("Nama mahasiswa: ")
    ipk = float(input("IPK mahasiswa: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat beasiswa.")
        continue

    penghasilan = int(input("Penghasilan orang tua per bulan (Rp): "))

    if penghasilan <= 3000000:
        beasiswa = "Beasiswa penuh"
        jumlah_penuh += 1
    elif penghasilan <= 5000000:
        beasiswa = "Beasiswa sebagian"
    else:
        beasiswa = "Tidak mendapatkan beasiswa"

    print("Nama:", nama)
    print("IPK:", ipk)
    print("Penghasilan orang tua: Rp", penghasilan)
    print("Hasil seleksi:", beasiswa)

print("\nJumlah penerima beasiswa penuh:", jumlah_penuh)
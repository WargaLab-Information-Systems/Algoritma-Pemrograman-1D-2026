jumlah_beasiswa_penuh = 0
jumlah_beasiswa_sebagian = 0
jumlah_tidak_mendapatkan = 0
jumlah_tidak_memenuhi_syarat = 0

for i in range(1, 11):
    if jumlah_beasiswa_penuh == 3:
        print("\nKuota beasiswa penuh telah terpenuhi.")
        break

    print("\nMahasiswa ke-", i)

    nama = input("Nama mahasiswa: ")
    ipk = float(input("IPK: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat karena IPK di bawah 3,00.")
        jumlah_tidak_memenuhi_syarat += 1
        continue

    penghasilan = float(input("Penghasilan orang tua per bulan (Rp): "))

    if penghasilan <= 3000000:
        status = "Beasiswa penuh"
        jumlah_beasiswa_penuh += 1
    elif penghasilan <= 5000000:
        status = "Beasiswa sebagian"
        jumlah_beasiswa_sebagian += 1
    else:
        status = "Tidak mendapatkan beasiswa"
        jumlah_tidak_mendapatkan += 1

    print("Nama:", nama)
    print("IPK:", ipk)
    print("Penghasilan orang tua: Rp", penghasilan)
    print("Hasil seleksi:", status)

print("\n=== REKAP SELEKSI BEASISWA ===")
print("Beasiswa penuh:", jumlah_beasiswa_penuh)
print("Beasiswa sebagian:", jumlah_beasiswa_sebagian)
print("Tidak mendapatkan beasiswa:", jumlah_tidak_mendapatkan)
print("Tidak memenuhi syarat IPK:", jumlah_tidak_memenuhi_syarat)

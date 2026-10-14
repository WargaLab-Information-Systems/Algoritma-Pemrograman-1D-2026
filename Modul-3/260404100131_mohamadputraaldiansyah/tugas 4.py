JUMLAH_MAHASISWA = 10
KUOTA_PENUH = 3

jumlah_penuh = 0
jumlah_sebagian = 0
jumlah_tidak = 0
jumlah_diproses = 0

for i in range(1, JUMLAH_MAHASISWA + 1):
    print("\nMahasiswa ke-", i)
    nama = input("Nama: ")

    while True:
        try:
            ipk = float(input("IPK: "))
            if 0 <= ipk <= 4:
                break
            print("IPK harus antara 0 sampai 4!")
        except ValueError:
            print("Harus berupa angka!")

    while True:
        try:
            penghasilan = float(input("Penghasilan orang tua   : Rp"))
            if penghasilan >= 0:
                break
            print("Penghasilan tidak boleh negatif!")
        except ValueError:
            print("Harus angka!")

    jumlah_diproses += 1

    if ipk < 3.00:
        print(f"Hasil: {nama} TIDAK memenuhi syarat (IPK di bawah 3,00).")
        jumlah_tidak += 1
        continue

    if penghasilan <= 3000000:
        print(f"Hasil: {nama} mendapat BEASISWA PENUH.")
        jumlah_penuh += 1
    elif penghasilan <= 5000000:
        print(f"Hasil: {nama} mendapat BEASISWA SEBAGIAN.")
        jumlah_sebagian += 1
    else:
        print(f"Hasil: {nama} TIDAK mendapat beasiswa (penghasilan terlalu tinggi).")
        jumlah_tidak += 1

    
    if jumlah_penuh == KUOTA_PENUH:
        print("\nKuota beasiswa penuh sudah terpenuhi. Seleksi dihentikan.")
        break


print("\n=== Rekap Seleksi ===")
print("Mahasiswa diproses    :", jumlah_diproses)
print("Beasiswa penuh        :", jumlah_penuh)
print("Beasiswa sebagian     :", jumlah_sebagian)
print("Tidak mendapat        :", jumlah_tidak)
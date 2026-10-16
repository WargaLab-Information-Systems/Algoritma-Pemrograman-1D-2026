jumlah_beasiswa_penuh = 0

print("=== Seleksi Awal Penerima Beasiswa ===")
for i in range(1, 11):
    print(f"\n--- Mahasiswa ke-{i} ---")
    nama = input("Nama                               : ")
    ipk = float(input("IPK                                : "))
    penghasilan = int(input("Penghasilan orang tua per bulan (Rp): "))

    if ipk < 3.00:
        print(f"Hasil: {nama} tidak memenuhi syarat (IPK kurang dari 3,00).")
        continue

    if penghasilan <= 3000000:
        print(f"Hasil: {nama} mendapatkan beasiswa PENUH.")
        jumlah_beasiswa_penuh += 1
        if jumlah_beasiswa_penuh == 3:
            print("\nKuota beasiswa penuh (3 mahasiswa) telah terpenuhi.")
            print("Proses seleksi dihentikan.")
            break
    elif penghasilan <= 5000000:
        print(f"Hasil: {nama} mendapatkan beasiswa SEBAGIAN.")
    else:
        print(f"Hasil: {nama} tidak mendapatkan beasiswa (penghasilan orang tua terlalu tinggi).")
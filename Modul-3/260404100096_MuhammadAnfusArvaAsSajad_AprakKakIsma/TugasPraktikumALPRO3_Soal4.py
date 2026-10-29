kuotaPenuh = 3
jumlahPenuh = 0
jumlahSebagian = 0
jumlahTidakDapat = 0
jumlahTidakMemenuhi = 0
jumlahDiproses = 0

print("=== SELEKSI AWAL PENERIMA BEASISWA ===")

for i in range(1, 11):
    print(f"\nData mahasiswa ke-{i}")
    nama = input("Nama                      : ")
    ipk = float(input("IPK                       : "))

    jumlahDiproses += 1

    if ipk < 3.00:
        print(f"Hasil: {nama} TIDAK MEMENUHI SYARAT (IPK < 3,00)")
        jumlahTidakMemenuhi += 1
        continue

    penghasilan = int(input("Penghasilan orang tua/bln : Rp"))

    if penghasilan <= 3000000:
        print(f"Hasil: {nama} mendapatkan BEASISWA PENUH")
        jumlahPenuh += 1
    elif penghasilan <= 5000000:
        print(f"Hasil: {nama} mendapatkan BEASISWA SEBAGIAN")
        jumlahSebagian += 1
    else:
        print(f"Hasil: {nama} TIDAK MENDAPATKAN BEASISWA")
        jumlahTidakDapat += 1

    if jumlahPenuh == kuotaPenuh:
        print("\nKuota beasiswa penuh telah terpenuhi, seleksi dihentikan!")
        break

print("\n=== REKAP SELEKSI ===")
print("Mahasiswa diproses        :", jumlahDiproses)
print("Beasiswa penuh            :", jumlahPenuh)
print("Beasiswa sebagian         :", jumlahSebagian)
print("Tidak mendapat beasiswa   :", jumlahTidakDapat)
print("Tidak memenuhi syarat IPK :", jumlahTidakMemenuhi)
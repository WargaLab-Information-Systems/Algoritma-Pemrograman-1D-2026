jumlahA = jumlahB = jumlahC = jumlahD = jumlahE = 0
totalNilai = 0
nilaiTertinggi = -1
nilaiTerendah = 101
namaTertinggi = ""
namaTerendah = ""

print("=== PENGELOLAAN NILAI MAHASISWA (10 MAHASISWA) ===")

for i in range(1, 11):
    print(f"\nData mahasiswa ke-{i}")
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    nilaiAkhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if nilaiAkhir >= 85:
        kategori = "A"
        jumlahA += 1
    elif nilaiAkhir >= 75:
        kategori = "B"
        jumlahB += 1
    elif nilaiAkhir >= 65:
        kategori = "C"
        jumlahC += 1
    elif nilaiAkhir >= 50:
        kategori = "D"
        jumlahD += 1
    else:
        kategori = "E"
        jumlahE += 1

    totalNilai += nilaiAkhir

    if nilaiAkhir > nilaiTertinggi:
        nilaiTertinggi = nilaiAkhir
        namaTertinggi = nama
    if nilaiAkhir < nilaiTerendah:
        nilaiTerendah = nilaiAkhir
        namaTerendah = nama

    print("--- Hasil ---")
    print(f"Nama        : {nama}")
    print(f"Tugas       : {tugas}")
    print(f"UTS         : {uts}")
    print(f"UAS         : {uas}")
    print(f"Nilai Akhir : {nilaiAkhir:.2f}")
    print(f"Kategori    : {kategori}")

rataRata = totalNilai / 10

print("\n=== REKAP KELAS ===")
print("Jumlah nilai A :", jumlahA)
print("Jumlah nilai B :", jumlahB)
print("Jumlah nilai C :", jumlahC)
print("Jumlah nilai D :", jumlahD)
print("Jumlah nilai E :", jumlahE)
print(f"Nilai tertinggi : {nilaiTertinggi:.2f} ({namaTertinggi})")
print(f"Nilai terendah  : {nilaiTerendah:.2f} ({namaTerendah})")
print(f"Rata-rata kelas : {rataRata:.2f}")
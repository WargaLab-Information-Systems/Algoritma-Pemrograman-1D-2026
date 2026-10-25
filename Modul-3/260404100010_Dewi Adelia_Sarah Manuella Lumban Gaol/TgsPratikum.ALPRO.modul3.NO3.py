
jumlah_A = 2
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total_nilai = 0
nilai_tertinggi = -1
nilai_terendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 11):
    print("\nMahasiswa ke-", i)

    nama = input("Masukkan nama: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    total_nilai += nilai_akhir

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

    print("\nHasil nilai mahasiswa:")
    print("Nama:", nama)
    print("Nilai tugas:", int(tugas))
    print("Nilai UTS:", int(uts))
    print("Nilai UAS:", int(uas))
    print("Nilai akhir:", round(nilai_akhir, 2))
    print("Kategori:", kategori)

rata_rata = total_nilai / 10

print("\n=== REKAPITULASI NILAI ===")
print("Jumlah mahasiswa kategori A:", jumlah_A)
print("Jumlah mahasiswa kategori B:", jumlah_B)
print("Jumlah mahasiswa kategori C:", jumlah_C)
print("Jumlah mahasiswa kategori D:", jumlah_D)
print("Jumlah mahasiswa kategori E:", jumlah_E)

print("\nNilai akhir tertinggi:", round(nilai_tertinggi, 2))
print("Nama mahasiswa:", nama_tertinggi)

print("\nNilai akhir terendah:", round(nilai_terendah, 2))
print("Nama mahasiswa:", nama_terendah)

print("\nRata-rata nilai akhir:", round(rata_rata, 2))

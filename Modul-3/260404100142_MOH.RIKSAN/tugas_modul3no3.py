jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total_nilai_akhir = 0
nilai_tertinggi = 0
nama_tertinggi = ""
nilai_terendah = 0
nama_terendah = ""

print("=== Pengelolaan Nilai Mahasiswa (10 Mahasiswa) ===")
for i in range(1, 11):
    print(f"\n--- Data mahasiswa ke-{i} ---")
    nama = input("Nama        : ")
    tugas = float(input("Nilai tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

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

    print("\nHasil:")
    print("Nama        :", nama)
    print("Nilai tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print(f"Nilai akhir : {nilai_akhir:.2f}")
    print("Kategori    :", kategori)

    total_nilai_akhir += nilai_akhir
    if i == 1 or nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama
    if i == 1 or nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

print("\n=== Rekap Seluruh Mahasiswa ===")
print("Jumlah mahasiswa kategori A:", jumlah_A)
print("Jumlah mahasiswa kategori B:", jumlah_B)
print("Jumlah mahasiswa kategori C:", jumlah_C)
print("Jumlah mahasiswa kategori D:", jumlah_D)
print("Jumlah mahasiswa kategori E:", jumlah_E)
print(f"Nilai akhir tertinggi : {nilai_tertinggi:.2f} ({nama_tertinggi})")
print(f"Nilai akhir terendah  : {nilai_terendah:.2f} ({nama_terendah})")
print(f"Rata-rata nilai akhir : {total_nilai_akhir / 10:.2f}")
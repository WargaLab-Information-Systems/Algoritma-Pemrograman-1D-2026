daftar_nama = []
daftar_tugas = []
daftar_uts = []
daftar_uas = []
daftar_akhir = []
daftar_kategori = []

while True:
    nama = input("Masukkan nama mahasiswa (atau ketik 'selesai' untuk berhenti): ")
    if nama.lower() == 'selesai':
        break

    try:
        tugas = float(input("Masukkan nilai tugas: "))
        uts = float(input("Masukkan nilai UTS: "))
        uas = float(input("Masukkan nilai UAS: "))
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
        continue

    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

    if nilai_akhir >= 85:
        kategori = "A"
    elif nilai_akhir >= 70:
        kategori = "B"
    elif nilai_akhir >= 55:
        kategori = "C"
    elif nilai_akhir >= 40:
        kategori = "D"
    else:
        kategori = "E"

    daftar_nama.append(nama)
    daftar_tugas.append(tugas)
    daftar_uts.append(uts)
    daftar_uas.append(uas)
    daftar_akhir.append(nilai_akhir)
    daftar_kategori.append(kategori)

print("\n=== Rekap Nilai Mahasiswa ===")
for i in range(len(daftar_nama)):
    print(f"Nama: {daftar_nama[i]}")
    print(f"Nilai Tugas: {daftar_tugas[i]}")
    print(f"Nilai UTS: {daftar_uts[i]}")
    print(f"Nilai UAS: {daftar_uas[i]}")
    print(f"Nilai Akhir: {daftar_akhir[i]:.2f}")
    print(f"Kategori: {daftar_kategori[i]}")
    print("-" * 30)
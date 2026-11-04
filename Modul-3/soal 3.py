jumlah_mhs = 10
hitung = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
total_nilai = 0
tertinggi = -1
terendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, jumlah_mhs + 1):
    print("Data Mahasiswa ke-" + str(i) + " ---")
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if akhir >= 85:
        kategori = "A"
    elif akhir >= 75:
        kategori = "B"
    elif akhir >= 65:
        kategori = "C"
    elif akhir >= 50:
        kategori = "D"
    else:
        kategori = "E"

    hitung[kategori] += 1
    total_nilai += akhir

    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama
    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

    akhir_bulat = int(akhir * 100 + 0.5) / 100
    print("Nama: " + nama + " | Tugas: " + str(tugas) + " | UTS: " + str(uts) + " | UAS: " + str(uas) + " | Akhir: " + str(akhir_bulat) + " | Kategori: " + kategori)

rata_rata = int(total_nilai / jumlah_mhs * 100 + 0.5) / 100
tinggi_bulat = int(tertinggi * 100 + 0.5) / 100
rendah_bulat = int(terendah * 100 + 0.5) / 100

print("===== REKAP NILAI KELAS =====")
for k in hitung:
    print("Jumlah mahasiswa nilai " + k + " : " + str(hitung[k]))
print("Nilai akhir tertinggi : " + str(tinggi_bulat) + " (" + nama_tertinggi + ")")
print("Nilai akhir terendah  : " + str(rendah_bulat) + " (" + nama_terendah + ")")
print("Rata-rata nilai akhir : " + str(rata_rata))
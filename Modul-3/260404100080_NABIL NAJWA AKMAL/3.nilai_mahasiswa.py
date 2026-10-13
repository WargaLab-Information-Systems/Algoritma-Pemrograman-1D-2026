nama = []
nilai_akhir = []

jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

for i in range(10):
    print("Mahasiswa ke-", i + 1)
    nama_mhs = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    akhir = (tugas * 30 + uts * 30 + uas * 40) / 100

    if akhir >= 85:
        kategori = "A"
        jumlah_A = jumlah_A + 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B = jumlah_B + 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C = jumlah_C + 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D = jumlah_D + 1
    else:
        kategori = "E"
        jumlah_E = jumlah_E + 1

    print("Nama:", nama_mhs)
    print("Nilai Tugas:", tugas)
    print("Nilai UTS:", uts)
    print("Nilai UAS:", uas)
    print("Nilai Akhir:", akhir)
    print("Kategori:", kategori)
    print("")

    nama.append(nama_mhs)
    nilai_akhir.append(akhir)

tertinggi = nilai_akhir[0]
terendah = nilai_akhir[0]
nama_tertinggi = nama[0]
nama_terendah = nama[0]

for i in range(10):
    if nilai_akhir[i] > tertinggi:
        tertinggi = nilai_akhir[i]
        nama_tertinggi = nama[i]
    if nilai_akhir[i] < terendah:
        terendah = nilai_akhir[i]
        nama_terendah = nama[i]

total = 0
for i in range(10):
    total = total + nilai_akhir[i]

rata_rata = total / 10

print("Jumlah mahasiswa nilai A:", jumlah_A)
print("Jumlah mahasiswa nilai B:", jumlah_B)
print("Jumlah mahasiswa nilai C:", jumlah_C)
print("Jumlah mahasiswa nilai D:", jumlah_D)
print("Jumlah mahasiswa nilai E:", jumlah_E)
print("Nilai akhir tertinggi:", tertinggi, "oleh", nama_tertinggi)
print("Nilai akhir terendah:", terendah, "oleh", nama_terendah)
print("Rata-rata nilai akhir:", rata_rata)

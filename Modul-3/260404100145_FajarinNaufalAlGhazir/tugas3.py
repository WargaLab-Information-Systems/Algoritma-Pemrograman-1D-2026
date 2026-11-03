jumlahMahasiswa = 0
totalNilai = 0
kategoriA = 0
kategoriB = 0
kategoriC = 0
kategoriD = 0
kategoriE = 0
naTertinggi = 0
naTerendah = 100
namaTertinggi = ""
namaTerendah = ""

for i in range(1, 11):
    print(f"Mahasiswa ke- {i}")
    namaMahasiswa = input("Masukkan nama Mahasiswa: ")
    nilaiTugas = float(input("Masukkan nilai tugas: "))
    nilaiUts = float(input("Masukkan nilai UTS: "))
    nilaiUas = float(input("Masukkan nilai UAS: "))

    jumlahMahasiswa += 1

    tugas = nilaiTugas * (30/100)
    uts = nilaiUts * (30/100)
    uas = nilaiUas * (40/100)
    nilaiAkhir = tugas + uts + uas
    totalNilai += nilaiAkhir

    if nilaiAkhir >= 85:
        kategori = "A"
        kategoriA += 1
    elif nilaiAkhir >= 75:
        kategori = "B"
        kategoriB += 1
    elif nilaiAkhir >= 65:
        kategori = "C"
        kategoriC += 1
    elif nilaiAkhir >= 50:
        kategori = "D"
        kategoriD += 1
    else:
        kategori = "E"
        kategoriE += 1

    print("-" * 40)
    print(f"Nama        : {namaMahasiswa}")
    print(f"Nilai tugas : {nilaiTugas}")
    print(f"Nilai UTS   : {nilaiUts}")
    print(f"Nilai UAS   : {nilaiUas}")
    print(f"Nilai akhir : {nilaiAkhir}")
    print(f"Kategori    : {kategori}")
    print("-" * 40)

    if nilaiAkhir > naTertinggi:
        naTertinggi = nilaiAkhir
        namaTertinggi = namaMahasiswa
    if nilaiAkhir < naTerendah:
        naTerendah = nilaiAkhir
        namaTerendah = namaMahasiswa

rataRataNilai = totalNilai / jumlahMahasiswa

print("-" * 50)
print(f"Jumlah mahasiswa nilai A: {kategoriA}")
print(f"Jumlah mahasiswa nilai B: {kategoriB}")
print(f"Jumlah mahasiswa nilai C: {kategoriC}")
print(f"Jumlah mahasiswa nilai D: {kategoriD}")
print(f"Jumlah mahasiswa nilai E: {kategoriE}")
print(f"Nilai akhir tertinggi   : {naTertinggi} ({namaTertinggi})")
print(f"Nilai akhir terendah    : {naTerendah} ({namaTerendah})")
print(f"Rata-rata nilai         : {rataRataNilai}")
print("-" * 50)
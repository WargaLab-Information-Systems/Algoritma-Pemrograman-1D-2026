gradeA = 0
gradeB = 0
gradeC = 0
gradeD = 0
gradeE = 0
nilaiTertinggi = 0
namaTertinggi = ""
nilaiTerendah = 100
namaTerendah = ""
totalNilaiAkhir = 0

for i in range(1, 11):
    namaMahasiswa = input("Masukkan nama mahasiswa: ")
    nilaiTugas = int(input("Masukkan nilai tugas: "))
    nilaiUts = int(input("Masukkan nilai UTS: "))
    nilaiUas = int(input("Masukkan nilai UAS: "))
    
    nilaiAkhir = ( nilaiTugas * (30/100) ) + ( nilaiUts * (30/100) ) + ( nilaiUas * (40/100) )
    totalNilaiAkhir += nilaiAkhir


    if nilaiAkhir == 90:
        grade = "A"
        gradeA += 1
    elif nilaiAkhir >= 75:
        grade = "B"
        gradeB += 1
    elif nilaiAkhir >= 65:
        grade = "C"
        gradeC += 1
    elif nilaiAkhir >= 50:
        grade = "D"
        gradeD += 1
    else:
        grade = "E"
        gradeE += 1

    if nilaiAkhir > nilaiTertinggi:
        nilaiTertinggi = nilaiAkhir
        namaTertinggi = namaMahasiswa

    if nilaiAkhir < nilaiTerendah:
        nilaiTerendah = nilaiAkhir
        namaTerendah = namaMahasiswa


    print("Nama Mahasiswa   :", namaMahasiswa)
    print("Nilai Tugas      :", nilaiTugas)
    print("Nilai UTS        :", nilaiUts)
    print("Nilai UAS        :", nilaiUas)
    print("Nilai Akhir      :", nilaiAkhir)
    print("Grade            :", grade)

print("_" * 20)


print("Grade A:", gradeA)
print("Grade B:", gradeB)
print("Grade C:", gradeC)
print("Grade D:", gradeD)
print("Grade E:", gradeE) 

print("Nilai akhir tertinggi: ", nilaiTertinggi)
print("Nama nilai akhir tertinggi: ", namaTertinggi)

print("Nilai akhir terendah: ", nilaiTerendah)
print("Nama nilai akhir terendah: ", namaTerendah)

rataRata = totalNilaiAkhir / 10
print("Nilai rata rata: ", rataRata)
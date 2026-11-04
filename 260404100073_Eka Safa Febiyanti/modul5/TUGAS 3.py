def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "A" or grade == "B" or grade == "C":
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    print("Nama Mahasiswa:", nama)
    print("Nilai Akhir:", nilai_akhir)
    print("Grade:", grade)
    print("Status:", status)

nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

hitung_nilai(nama, tugas, uts, uas)
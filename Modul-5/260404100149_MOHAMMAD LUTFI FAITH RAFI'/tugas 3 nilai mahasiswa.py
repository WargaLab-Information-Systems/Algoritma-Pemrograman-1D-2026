def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if nilai_akhir >= 85:
        grade = "A"
        status = "Lulus"
    elif nilai_akhir >= 70:
        grade = "B"
        status = "Lulus"
    elif nilai_akhir >= 55:
        grade = "C"
        status = "Lulus"
    else:
        grade = "D"
        status = "Tidak Lulus"

    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas    :", tugas)
    print("Nilai UTS      :", uts)
    print("Nilai UAS      :", uas)
    print("Nilai Akhir    :", nilai_akhir)
    print("Grade          :", grade)
    print("Status         :", status)

nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

hitung_nilai(nama, tugas, uts, uas)
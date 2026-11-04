nama = input("masukkan nama: ")
tugas = float(input("masukkan nilai tugas: "))
uts = float(input("masukkan nilai uts: "))
uas = float(input("masukkan nilai uas: "))

def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = (tugas * 30/100) + (uts * 30/100) + (uas * 40/100)

    if nilai_akhir >= 85:
        grade = "A"
        status = "lulus"
    elif nilai_akhir >= 70:
        grade = "B"
        status = "lulus"
    elif nilai_akhir >= 55:
        grade = "C"
        status = "lulus"            
    else:
        grade = "D"
        status = "tidak lulus"

    print("nama : ", nama)
    print("nilai akhir : ", nilai_akhir)
    print("grade", grade, "status", status)

hitung_nilai(nama, tugas, uts, uas)
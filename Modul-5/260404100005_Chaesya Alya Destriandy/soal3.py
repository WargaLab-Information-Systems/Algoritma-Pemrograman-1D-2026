# Input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

def nilai_mahasiswa(nama, tugas, uts, uas):
    # Menghitung nilai akhir berdasarkan bobot
    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    # Menentukan grade
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    # Menentukan status kelulusan
    if grade == "A" or grade == "B" or grade == "C":
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    # Menampilkan hasil
    print("\n=== Hasil Nilai Mahasiswa ===")
    print("Nama         :", nama)
    print("Nilai Tugas  :", tugas)
    print("Nilai UTS    :", uts)
    print("Nilai UAS    :", uas)
    print("Nilai Akhir  :", round(nilai_akhir, 2))
    print("Grade        :", grade)
    print("Status       :", status)

# Memanggil function
nilai_mahasiswa(nama, tugas, uts, uas)

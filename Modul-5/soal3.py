def nilai_akhir(nama, tugas, uts, uas):
    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas
 
    if akhir >= 85:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"
 
    if grade == "D":
        keterangan = "Tidak Lulus"
    else:
        keterangan = "Lulus"
 
    print("Nama        :", nama)
    print("Nilai Tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai Akhir :", akhir)
    print("Grade       :", grade)
    print("Keterangan  :", keterangan)
 
nama = input("Masukkan nama mahasiswa : ")
tugas = float(input("Masukkan nilai tugas : "))
uts = float(input("Masukkan nilai UTS : "))
uas = float(input("Masukkan nilai UAS : "))
nilai_akhir(nama, tugas, uts, uas)
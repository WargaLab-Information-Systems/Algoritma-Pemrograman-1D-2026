def hitung_nilai(nama, tugas, uts, uas):
    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if akhir >= 85:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    status = "Lulus" if grade in ("A", "B", "C") else "Tidak Lulus"

    print("Nama        :", nama)
    print("Nilai Tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print(f"Nilai Akhir : {akhir}")
    print("Grade       :", grade)
    print("Status      :", status)

nama = input("Nama mahasiswa: ")
tugas =  float(input("Nilai tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))
hitung_nilai(nama, tugas, uts, uas)
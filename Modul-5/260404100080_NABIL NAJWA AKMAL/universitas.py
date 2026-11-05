def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print("\n=== Hasil Perhitungan ===")
    print("Nama        :", nama)
    print("Nilai Tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai Akhir :", round(nilai_akhir, 2))
    print("Grade       :", grade)
    print("Status      :", status)

nama = input("Nama mahasiswa: ")
tugas = float(input("Nilai tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

hitung_nilai(nama, tugas, uts, uas)

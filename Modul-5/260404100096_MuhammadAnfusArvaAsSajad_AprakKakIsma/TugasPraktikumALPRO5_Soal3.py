def hitungNilaiAkhir(nama, tugas, uts, uas):
    tugas = float(input("Nilai tugas    : "))
    uts = float(input("Nilai UTS      : "))
    uas = float(input("Nilai UAS      : "))

    nilaiAkhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if nilaiAkhir >= 85:
        grade = "A"
    elif nilaiAkhir >= 70:
        grade = "B"
    elif nilaiAkhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print("\n=== HASIL PERHITUNGAN NILAI AKHIR ===")
    print(f"Nama        : {nama}")
    print(f"Nilai Tugas : {tugas}")
    print(f"Nilai UTS   : {uts}")
    print(f"Nilai UAS   : {uas}")
    print(f"Nilai Akhir : {nilaiAkhir:.2f}")
    print(f"Grade       : {grade}")
    print(f"Status      : {status}")




hitungNilaiAkhir(nama, tugas, uts, uas)
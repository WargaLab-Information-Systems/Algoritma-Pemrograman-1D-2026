def nilai(namaMahasiswa, nilaiTugas, nilaiUts, nilaiUas):
    nilaiAkhir = ( nilaiTugas * (30/100) ) + ( nilaiUts * (30/100) ) + ( nilaiUas * (40/100) )

    if nilaiAkhir >= 85:
        grade = "A"
    elif nilaiAkhir >= 70:
        grade = "B"
    elif nilaiAkhir >= 55:
        grade = "C"
    else:
        grade = "D"
        
    status = "Tidak Lulus!" if grade == "D" else "Lulus!"
    

    print("Nama Mahasiswa :", namaMahasiswa)
    print("Nilai Tugas    :", nilaiTugas)
    print("Nilai UTS      :", nilaiUts)
    print("Nilai UAS      :", nilaiUas)
    print("Nilai Akhir    :", nilaiAkhir)
    print("Grade          :", grade)
    print("Status         :", status)
    
namaMahasiswa = input("Masukkan nama mahasiswa  : ")
nilaiTugas = int(input("Masukkan nilai tugas    : "))
nilaiUts = int(input("Masukkan nilai UTS        : "))
nilaiUas = int(input("Masukkan nilai UAS        : "))

nilai(namaMahasiswa, nilaiTugas, nilaiUts, nilaiUas)
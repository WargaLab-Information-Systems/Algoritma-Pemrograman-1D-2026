def nilai_akhir():
    ntugas=int(input("masukkan nilai tugas:"))
    nUTS=int(input("masukkan nilai UTS:"))
    nUAS=int(input("Masukkan nilai UAS:"))
    nilaiakhir= ntugas * 0.3 + nUTS * 0.3 + nUAS * 0.4
    print("hasil nilai:",nilaiakhir)

    if nilaiakhir >= 85:
        return "Grade A"
    elif nilaiakhir >= 70:
        return "Grade B"
    elif nilaiakhir >= 55:
        return "Grade C"
    else:
        return "Tidak Lulus"

print(nilai_akhir())
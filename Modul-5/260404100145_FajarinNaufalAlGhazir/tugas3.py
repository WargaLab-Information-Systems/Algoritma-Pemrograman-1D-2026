def hitungNilai(tugas, uts, uas):
    return (tugas * 30/100) + (uts * 30/100) + (uas * 40/100)

def tentukanGrade(nilaiAkhir):
    if nilaiAkhir >= 85:
        return "A"
    elif nilaiAkhir >= 70:
        return "B"
    elif nilaiAkhir >= 55:
        return "C"
    else:
        return "D"

status = lambda grade: "Tidak Lulus" if grade == "D" else "Lulus"

def output(nama, tugas, uts, uas):
    nilaiAkhir = hitungNilai(tugas, uts, uas)
    grade = tentukanGrade(nilaiAkhir)
    
    print(f"Nama        : {nama}")
    print(f"Nilai       : {nilaiAkhir}")
    print(f"Grade       : {grade}")
    print(f"Status      : {status(grade)}")
    print("-" * 30)

def main():
    nomor = 2
    while True:
        nama = input("Masukkan nama : ")
        tugas = float(input("Nilai tugas   : "))
        uts = float(input("Nilai UTS     : "))
        uas = float(input("Nilai UAS     : "))
        print("-" * 30)

        output(nama, tugas, uts, uas)

        lanjut = input(f"Lanjut mahasiswa ke-{nomor}? (y/n) ")

        if lanjut == "n" or lanjut == "N":
            break
        else:
            nomor += 1

main()
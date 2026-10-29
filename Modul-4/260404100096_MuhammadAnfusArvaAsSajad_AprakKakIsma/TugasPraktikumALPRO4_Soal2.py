gajiPokok = 100000
tambahanShiftMalam = 50000
totalGaji = 0
totalLembur = 0
totalShift = 0

print("=== PERHITUNGAN GAJI MINGGUAN KARYAWAN ===")

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")

    jamLembur = int(input("Jam lembur (0 jika tidak lembur) : "))
    while jamLembur < 0 or jamLembur == 5 or jamLembur == 7:
        print("Jam lembur tidak sesuai ketentuan, silakan ulangi!")
        jamLembur = int(input("Jam lembur (0 jika tidak lembur) : "))

    if jamLembur == 0:
        upahLembur = 0
    elif jamLembur <= 3:
        upahLembur = jamLembur * 25000
    elif jamLembur == 4:
        upahLembur = 100000
    elif jamLembur == 6:
        upahLembur = 200000
    elif jamLembur == 8:
        upahLembur = 300000
    else:
        upahLembur = 0
        print("Jumlah lembur melebihi batas yang ditentukan, upah lembur tidak dihitung!")

    shift = input("Shift malam? (y/n)               : ").lower()
    while shift != "y" and shift != "n":
        print("Input tidak valid, ketik y atau n!")
        shift = input("Shift malam? (y/n)               : ").lower()

    if shift == "y":
        upahShift = tambahanShiftMalam
    else:
        upahShift = 0

    gajiHari = gajiPokok + upahLembur + upahShift
    print(f"Gaji hari ke-{hari}: Rp{gajiHari:,}".replace(",", "."))

    totalGaji += gajiHari
    totalLembur += upahLembur
    totalShift += upahShift

print("\n=== RINCIAN GAJI MINGGUAN ===")
print("Gaji pokok (7 hari) : Rp" + f"{gajiPokok * 7:,}".replace(",", "."))
print("Total upah lembur   : Rp" + f"{totalLembur:,}".replace(",", "."))
print("Total tambahan malam: Rp" + f"{totalShift:,}".replace(",", "."))
print("Total gaji mingguan : Rp" + f"{totalGaji:,}".replace(",", "."))
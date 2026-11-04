total_gaji = 0

for hari in range(1, 8):
    print("\nHari ke-", hari)

    gaji_pokok = 100000

    while True:
        lembur = int(input("Masukkan jam lembur (0, 1, 2, 3, 4, 6, atau 8): "))

        if lembur > 8:
            print("Jam lembur melebihi batas yang ditentukan.")
            print("Silakan masukkan ulang data.")
        elif lembur not in [0, 1, 2, 3, 4, 6, 8]:
            print("Jumlah jam lembur tidak sesuai ketentuan.")
            print("Silakan masukkan ulang data.")
        else:
            break

    if lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    shift = input("Apakah bekerja shift malam? (y/t): ")

    if shift.lower() == "y":
        tambahan_shift = 50000
    else:
        tambahan_shift = 0

    gaji_harian = gaji_pokok + upah_lembur + tambahan_shift
    total_gaji += gaji_harian

    print("Gaji hari ini: Rp", gaji_harian)

print("\nTotal gaji selama 7 hari: Rp", total_gaji)

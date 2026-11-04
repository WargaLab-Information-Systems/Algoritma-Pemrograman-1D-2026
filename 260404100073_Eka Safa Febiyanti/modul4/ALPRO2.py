total_gaji = 0

for hari in range(1, 8):
    print("Hari ke-", hari)

    while True:
        lembur = int(input("Masukkan jam lembur: "))

        if lembur > 8:
            print("Jam lembur melebihi batas!")
        elif lembur < 0 or lembur == 5 or lembur == 7:
            print("Jam lembur tidak sesuai ketentuan!")
        else:
            break

    shift = input("Shift malam? (ya/tidak): ").lower()

    gaji_pokok = 100000

    if lembur >= 1 and lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    if shift == "ya":
        upah_malam = 50000
    else:
        upah_malam = 0

    gaji_harian = gaji_pokok + upah_lembur + upah_malam
    total_gaji = total_gaji + gaji_harian

    print("Gaji hari ini: Rp", gaji_harian)

print("Total gaji selama 7 hari: Rp", total_gaji)
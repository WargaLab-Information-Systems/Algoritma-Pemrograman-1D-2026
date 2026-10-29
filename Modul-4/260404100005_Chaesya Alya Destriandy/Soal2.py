total_gaji = 0

for hari in range(1, 3):
    print("\nHari ke-", hari)

    gaji_pokok = 100000

    while True:
        jam_lembur = int(input("Masukkan jam lembur: "))

        if jam_lembur < 0:
            print("Jam lembur tidak boleh negatif, masukkan ulang!")
        elif jam_lembur == 5 or jam_lembur == 7:
            print("Jam lembur tidak sesuai ketentuan, masukkan ulang!")
        else:
            break

    if jam_lembur >= 1 and jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000
    elif jam_lembur > 8:
        print("Jumlah lembur melebihi batas yang ditentukan!")
        upah_lembur = 0
    else:
        upah_lembur = 0 #kalau jam lemburnya 0

    shift_malam = input("Bekerja shift malam? (ya/tidak/iya/y): ")

    if shift_malam == "ya" or shift_malam == "iya" or shift_malam == "y":
        tambahan_shift = 50000
    else:
        tambahan_shift = 0

    gaji_harian = gaji_pokok + upah_lembur + tambahan_shift
    total_gaji = total_gaji + gaji_harian

    print("Gaji hari ini: Rp", gaji_harian)

print("\nTotal gaji mingguan: Rp", total_gaji)

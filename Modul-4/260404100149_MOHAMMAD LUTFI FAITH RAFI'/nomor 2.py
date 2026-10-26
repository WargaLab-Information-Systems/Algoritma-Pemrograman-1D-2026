total_gaji = 0

for hari in range(1, 8):
    print(f"Data hari ke-{hari}")

    gaji_pokok = 100000
    upah_lembur = 0
    tambahan_malam = 0

    while True:
        jam_lembur = int(input("Masukkan jam lembur (0, 1-4, 6, atau 8): "))

        if jam_lembur == 0:
            upah_lembur = 0
            break       
        elif jam_lembur >= 1 and jam_lembur <= 3:
            upah_lembur = jam_lembur * 25000
            break
        # elif jam_lembur >= 5 and jam_lembur <= 7: #just latihan dari mas nafis 
        #     upah_lembur = jam_lembur * 25000
        #     break
        elif jam_lembur == 4:
            upah_lembur = 100000
            break
        elif jam_lembur == 6:
            upah_lembur = 200000
            break
        elif jam_lembur == 8:
            upah_lembur = 300000
            break
        elif jam_lembur > 8:
            print("Jumlah lembur melebihi batas yang ditentukan.")
            print("Upah lembur tidak dihitung. Silakan masukkan ulang.")
        else:
            print("Jam lembur tidak sesuai ketentuan. Silakan masukkan ulang.")

    shift = input("Apakah bekerja shift malam? (ya/tidak): ").lower()

    if shift == "ya":
        tambahan_malam = 50000

    gaji_harian = gaji_pokok + upah_lembur + tambahan_malam
    total_gaji = total_gaji + gaji_harian

    print(f"Gaji pokok       : Rp{gaji_pokok}")
    print(f"Upah lembur      : Rp{upah_lembur}")
    print(f"Tambahan malam  : Rp{tambahan_malam}")
    print(f"Gaji hari ke-{hari}: Rp{gaji_harian}")

print("Total gaji mingguan: Rp", total_gaji)



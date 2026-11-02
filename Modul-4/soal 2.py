
GAJI_HARIAN = 100000
BONUS_MALAM = 50000
JUMLAH_HARI = 7

total = 0

for hari in range(1, JUMLAH_HARI + 1):
    print(f"\nHari ke-{hari}")

    while True:
        lembur = int(input("Jam lembur (0-8): "))
        if 0 <= lembur <= 8:
            break
        elif lembur > 8:
            print("Jumlah lembur melebihi batas yang ditentukan!")
        else:
            print("Jam lembur tidak sesuai ketentuan, ulangi!")

    if lembur == 0:
        upah = 0
    elif 1 <= lembur <= 3:
        upah_lembur = 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    else: lembur == 8
    upah_lembur = 300000

    malam = input("Shift malam (y/n): ").lower()
    bonus =BONUS_MALAM if malam == "y"  else 0

    total += GAJI_HARIAN + upah_lembur + bonus

print("\n=== TOTAL GAJI MINGGUAN ===")
print(f"Total gaji mingguan: Rp{total:,}")
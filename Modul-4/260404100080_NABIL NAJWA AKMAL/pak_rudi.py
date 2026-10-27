total_gaji = 0
gaji_utama = 100000

for i in range(1, 7 + 1):
    print(f"\nHari ke-{i}")
    total_gaji += gaji_utama
    bonus_shift = 0
    shift_kerja = input("masuk shift malam/pagi :").lower()
    if shift_kerja == "shift malam" or shift_kerja == "malam":
        total_gaji = total_gaji + 50000
        bonus_shift = 50000
    else:
        print("tdk mendapatkan tambahan gaji")
    while True:
        jam_lembur = int(input("masukkan jam lembur(0 jika tdk lembur) :"))
        if jam_lembur == 0:
            print ("tidak ada upah lembur hari ini")
            break
        elif jam_lembur >= 1 and jam_lembur <= 3:
            total_gaji = total_gaji + (25000 * jam_lembur)
            print(gaji_utama + bonus_shift + 25000 * jam_lembur)
            print()
            break
        elif jam_lembur == 4:
            print(gaji_utama + 100000)
            total_gaji = total_gaji + 100000
            break
        elif jam_lembur == 6:
            print(gaji_utama + 200000)
            total_gaji = total_gaji + 200000
            break
        elif jam_lembur == 8:
            print(gaji_utama + 300000)
            total_gaji = total_gaji + 300000
            break
        elif jam_lembur > 8:
            print("lembur melebihi batas yang ditentukan dan tidak menghitung upah lembur tersebut.")
            break
        else:
            print("jam lembur tidak memenuhi syarat (pilih 0,1-3, 4, 6, 8). silakan ulangi")

print(f"\njumlah total seluruh gaji karyawan selama 1 minggu adalah {total_gaji}")
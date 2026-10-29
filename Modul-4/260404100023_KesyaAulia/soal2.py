upah_lembur = 0 
shift_malam = 0
gaji_pokok = 0

for i in range(1, 8):
    print("hari ke ", i)
    jam_lembur = int(input("masukkan jumlah jam lembur karyawan: "))

    while jam_lembur <0 or jam_lembur > 8 or jam_lembur == 5 or jam_lembur == 7:
        print("jam lembur tidak sesuai ketentuan")
        jam_lembur = int(input("masukkan jumlah jam lembur karyawan: "))

    if jam_lembur >=1 and  jam_lembur <=3:
        lembur = 25000 * jam_lembur
    elif jam_lembur == 4:
        lembur = 100000
    elif jam_lembur == 6:
        lembur = 200000
    elif jam_lembur == 8:
        lembur = 300000 
    else:
        lembur = 0
        print("jumlah lembur melebihi batas.")

    upah_lembur += lembur

    malam = input("apakah kamu shift malam? ya/yes/tidak: ")
    if malam == "ya" or malam == "yes" or malam == "iya":
        shift_malam += 50000
    

    gaji_pokok += 100000

    print("upah lembur: ", upah_lembur )
    print("upah shift malam: ", shift_malam)
    print("gaji pokok: ", gaji_pokok)

total_gaji= upah_lembur + shift_malam + gaji_pokok

print("total gaji satu minggu: ", total_gaji)
print("total upah lembur: ", upah_lembur )
print("total upah shift malam: ", shift_malam)
print("total gaji pokok: ", gaji_pokok)



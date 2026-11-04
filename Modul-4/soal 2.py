GAJI_POKOK = 100000
TAMBAHAN_SHIFT_MALAM = 50000
total_gaji_mingguan = 0

print("=== Program Perhitungan Gaji Mingguan Karyawan ===")

for hari in range(1, 8):
    print()  
    print(f"Data Hari ke-{hari}:")
    
    
    while True:
        jam_lembur = int(input("Masukkan jam lembur (0-8 jam): "))
        if jam_lembur < 0:
            print("Jam lembur tidak boleh negatif. Silakan masukkan ulang.")
        elif jam_lembur > 8:
            print("Jumlah lembur melebihi batas yang ditentukan (maksimal 8 jam)! Silakan masukkan ulang.")
        else:
            break
            
   
    status_shift = input("Apakah bekerja pada shift malam? (y/n): ")
    
  
    gaji_harian = GAJI_POKOK
    if status_shift == 'y':
        gaji_harian += TAMBAHAN_SHIFT_MALAM
        
    
    upah_lembur = 0
    if 1 <= jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0 # Untuk 0 jam lembur
        
    
    total_harian = gaji_harian + upah_lembur
    total_gaji_mingguan += total_harian
    print(f"Total gaji hari ke-{hari}: Rp{total_harian:,}")

print()
print(f"==========================================")
print(f"Total Gaji Mingguan Karyawan: Rp{total_gaji_mingguan:,}")
print(f"==========================================")
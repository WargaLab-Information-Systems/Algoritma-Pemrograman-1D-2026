jumlah_target = 10
kuota_penuh_maks = 3
jumlah_beasiswa_penuh = 0

print("=== PROGRAM SELEKSI AWAL BEASISWA ===")
print(f"Kapasitas Kuota Beasiswa Penuh: {kuota_penuh_maks} orang dari {jumlah_target} pendaftar")

for i in range(1, jumlah_target + 1):
    print(f"--- Memproses Mahasiswa ke-{i} ---")

   
    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK (0.0 - 4.0): "))
    penghasilan = float(input("Masukkan penghasilan orang tua per bulan (Rp): "))

   
    if ipk < 3.00:
        print(f"-> Hasil {nama}: TIDAK MEMENUHI SYARAT (IPK {ipk:.2f} < 3.00). Dilewati")
        continue

   
    if penghasilan <= 3000000:
        status_beasiswa = "Beasiswa Penuh"
        jumlah_beasiswa_penuh += 1
    elif penghasilan <= 5000000:
        status_beasiswa = "Beasiswa Sebagian"
    else:
        status_beasiswa = "Tidak Mendapatkan Beasiswa"

   
    print(f"-> Hasil Seleksi {nama}: {status_beasiswa} (IPK: {ipk:.2f}, Penghasilan: Rp{penghasilan:,.0f})")

   
    if jumlah_beasiswa_penuh >= kuota_penuh_maks:
        print("[INFO] Kuota penerima beasiswa penuh telah terpenuhi (3 orang). Program seleksi dihentikan lebih awal.")
        break


print("=== LAPORAN AKHIR SELEKSI SELESAI ===")
print(f"Total mahasiswa yang berhasil mendapatkan beasiswa penuh: {jumlah_beasiswa_penuh} orang")
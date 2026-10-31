jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))

for baris in range(1, jumlah_baris + 1):
    print(f"Pemeriksaan baris ke-{baris}")

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"    Lampu nomor {lampu}: Mengalami gangguan")
        else:
            print(f"    Lampu nomor {lampu}: Berfungsi normal")

print("Periksa sumber listrik utama taman.")
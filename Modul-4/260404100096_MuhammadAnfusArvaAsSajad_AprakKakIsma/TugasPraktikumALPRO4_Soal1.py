jumlahBaris = int(input("Masukkan jumlah baris lampu    : "))
jumlahLampu = int(input("Masukkan jumlah lampu per baris: "))

print("\n=== PEMERIKSAAN LAMPU TAMAN KOTA ===")

for baris in range(1, jumlahBaris + 1):
    print(f"\nBaris ke-{baris}")
    for lampu in range(1, jumlahLampu + 1):
        if lampu % 3 == 0:
            print(f"  Lampu {lampu}: mengalami gangguan")
        else:
            print(f"  Lampu {lampu}: berfungsi normal")

print("\nSeluruh lampu sudah diperiksa. Segera periksa sumber listrik utama taman!")
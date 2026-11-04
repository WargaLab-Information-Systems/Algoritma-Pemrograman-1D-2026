jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))


for baris in range(1, jumlah_baris + 1):
    print()  
    print(f"--- Memeriksa Baris ke-{baris} ---")
    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu}: Mengalami gangguan")
        else:
            print(f"Lampu ke-{lampu}: Berfungsi normal")


print()
print("Semua lampu telah diperiksa. Silakan periksa sumber listrik utama taman!")
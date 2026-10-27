jum_baris = int(input("masukkan jumlah baris lampu :"))
jum_lampu = int(input("masukkan jumlah lampu setiap baris :"))

for i in range(1, jum_baris + 1):
    print(f"\nMemeriksa Baris ke-{i}")
    for k in range(1, jum_lampu + 1):
        if k % 3 == 0:
            print(f"lampu {k} mengalami gangguan")
        else:
            print(f"lampu {k} dinyatakan berfungsi normal.")
    print()

print("\nMemeriksa sumber listrik utama taman.")
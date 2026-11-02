jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))

for b in range(1, jumlah_baris + 1):
    print(f"baris {b}")
    for c in range(1, jumlah_lampu +1):
        if c % 3 == 0:
            print(f"    lampu {c}: sedang ganguan")
        else:
            print(f"    lampu {c}: berfungsi normal")
print("periksa sumber listrik teman")

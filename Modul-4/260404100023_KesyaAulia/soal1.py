
baris = int(input("Masukkan jumlah baris yang diinginkan: "))
lampu = int(input("Masukkan jumlah lampu yang diinginkan: "))

if baris <= 0 or lampu <= 0:
    print("Jumlah baris dan lampu harus lebih dari 0.")
else:
    for i in range(1, baris + 1):
        print()
        print(f"baris {i}")
        for j in range(1, lampu + 1):
            status = "normal" if j % 2 == 0 else "gangguan"
            print(f"{j} {status}, ", end="")
    print()
    print("Periksa sumber listrik utama taman")
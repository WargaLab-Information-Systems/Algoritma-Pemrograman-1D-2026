penuh = 0

for i in range(1, 11):
    print("Mahasiswa ke-", i)
    nama = input("Nama: ")
    ipk = float(input("IPK: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat, IPK kurang dari 3.00")
        continue

    penghasilan = int(input("Penghasilan orang tua per bulan: "))

    if penghasilan <= 3000000:
        if penuh < 3:
            penuh = penuh + 1
            print(nama, "mendapat beasiswa penuh")
        else:
            print(nama, "tidak dapat beasiswa penuh karena kuota habis")
    elif penghasilan <= 5000000:
        print(nama, "mendapat beasiswa sebagian")
    else:
        print(nama, "tidak mendapat beasiswa")

    if penuh == 3:
        print("Kuota beasiswa penuh sudah penuh, seleksi dihentikan")
        break

print("Total mahasiswa penerima beasiswa penuh:", penuh)

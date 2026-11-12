
def evaluasiPC(status, ram):
    ram = int(ram)

    if status == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"


daftarPC = []

jumlahPC = int(input("Masukkan jumlah PC: "))

for i in range(jumlahPC):
    print(f"\nData PC ke-{i + 1}")

    namaPC = input("Masukkan nama PC: ")
    status = input("Masukkan status PC (Normal/Rusak): ")
    ram = input("Masukkan kapasitas RAM (GB): ")

    daftarPC.append([namaPC, status, ram])


print("\n=== HASIL EVALUASI INVENTARIS PC ===")

for data in daftarPC:
    namaPC = data[0]
    status = data[1]
    ram = data[2]

    try:
        hasil = evaluasiPC(status, ram)
    except ValueError:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + namaPC + '", "Status": "' + hasil + '" }')
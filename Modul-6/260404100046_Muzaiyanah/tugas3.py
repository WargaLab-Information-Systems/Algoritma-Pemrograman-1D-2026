def evaluasi(status, ram):
    ramAngka = int(ram)  
    if status.lower() == "normal" and ramAngka >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

jumlah = int(input("Masukkan jumlah PC: "))

inventaris = []
for i in range(jumlah):
    print("\nData PC ke-" + str(i + 1))
    namaPC = input("Masukkan nama PC: ")
    status = input("Masukkan status (Normal/Rusak): ")
    ram = input("Masukkan kapasitas RAM (GB): ")
    inventaris.append([namaPC, status, ram])

print("\nHasil evaluasi:")
for data in inventaris:
    try:
        hasil = evaluasi(data[1], data[2])
    except ValueError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + data[0] + '", "Status": "' + hasil + '" }')
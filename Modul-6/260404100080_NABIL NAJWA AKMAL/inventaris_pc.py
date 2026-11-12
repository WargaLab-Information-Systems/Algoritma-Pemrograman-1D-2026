def cek_layak(status, ram):
    ram_angka = int(ram)
    if status == "Normal" and ram_angka >= 8:
        return "Layak"
    return "Tidak Layak"

jumlah = int(input("Masukkan jumlah PC: "))
inventaris = []

for i in range(jumlah):
    print("Data PC ke-", i + 1)
    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    inventaris.append([nama, status, ram])

for pc in inventaris:
    try:
        hasil = cek_layak(pc[1], pc[2])
    except ValueError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')

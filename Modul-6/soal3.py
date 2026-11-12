def cek_layak(pc):
    if pc[1] == "Normal" and pc[2] >= 8:
        return "Layak"
    return "Tidak Layak"

jumlah = int(input("Jumlah PC: "))
inventaris = []
for i in range(jumlah):
    nama = input(f"Nama PC ke-{i+1}: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    try:
        ram = int(ram)
    except ValueError:
        pass
    inventaris.append([nama, status, ram])

print("Hasil evaluasi:")
for pc in inventaris:
    try:
        hasil = cek_layak(pc)
    except TypeError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')

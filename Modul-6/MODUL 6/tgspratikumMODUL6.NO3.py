
def evaluasi_pc(status, ram):
    if status.lower() == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"


inventaris = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    inventaris.append([nama, status, ram])


print("Hasil Evaluasi Inventaris:")

for pc in inventaris:
    try:
        hasil = evaluasi_pc(pc[1], float(pc[2]))
    except (ValueError, TypeError):
        hasil = "Format RAM Kacau"

    output = '{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }'
    print(output)

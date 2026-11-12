data_pc = []
jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    data_pc.append([nama, status, ram])

def cek_kelayakan(status, ram):
    try:
        ram = int(ram)

        if status.lower() == "normal" and ram >= 8:
            return "Layak"
        else:
            return "Tidak Layak"

    except ValueError:
        return "Format RAM Kacau"

print("HASIL INVENTARIS PC")

for pc in data_pc:
    nama = pc[0]
    status = cek_kelayakan(pc[1], pc[2])

    hasil = '{"PC": "' + nama + '", "Status": "' + status + '"}'
    print(hasil)
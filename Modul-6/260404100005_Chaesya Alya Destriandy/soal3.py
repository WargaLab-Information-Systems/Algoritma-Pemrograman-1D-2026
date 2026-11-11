jumlah = int(input("Masukkan jumlah PC: "))

def evaluasi(pc):
    ram = int(pc[2])

    if pc[1] == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

data_pc = []

for i in range(jumlah):
    nama = input("Nama PC: ")
    status = input("Status PC (Normal/Rusak): ")
    ram = input("Kapasitas RAM: ")

    data_pc.append([nama, status, ram])


print("\nHasil Evaluasi:")


for pc in data_pc:
    try:
        hasil = evaluasi(pc)
    except ValueError:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')
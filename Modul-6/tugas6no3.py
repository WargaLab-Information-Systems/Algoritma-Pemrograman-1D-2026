pc = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama = input("Masukkan nama PC: ")
    status = input("Masukkan status PC (Normal/Rusak): ")
    ram = input("Masukkan kapasitas RAM: ")

    pc.append([nama, status, ram])

def evaluasi(status, ram):
    if status == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

print("Hasil Evaluasi:")

for data in pc:
    try:
        hasil = evaluasi(data[1], data[2])
    except TypeError:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + data[0] + '", "Status": "' + hasil + '" }')
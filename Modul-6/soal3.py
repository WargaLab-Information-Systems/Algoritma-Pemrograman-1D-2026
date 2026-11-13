def evaluasi(status, ram):
    ram_angka = int(ram)   
    if status == "Normal" and ram_angka >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

pc = []
jumlah = int(input("Jumlah PC: "))

for i in range(jumlah):
    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")   

    pc.append([nama, status, ram])


for data in pc:
    try:
        hasil = evaluasi(data[1], data[2])
    except ValueError:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + data[0] + '", "Status": "' + hasil + '" }')
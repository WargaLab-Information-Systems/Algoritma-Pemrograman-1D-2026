pendataan_pc = []

jumlah_pc = int(input("masukkan jumlah pc :"))
for i in range(jumlah_pc):
    data = []

    nama_pc = input("masukkan nama pc :")
    data.append(nama_pc)

    status_pc = input("masukkan status pc :")
    data.append(status_pc)

    ram = input("masukkan ram pc :")
    data.append(ram)

    pendataan_pc.append(data)

def evaluasi (status_pc, ram):
    ram = int(ram)
    if status_pc == "normal" and ram >= 8:
        return "layak"
    else:
        return "tidak layak"

for data in pendataan_pc:
    try:
        status = evaluasi(data[1], data[2])
    except:
        status = "format ram kacau"
    print('{ "PC": "' + data[0] + '", "Status": "' + status + '" }')

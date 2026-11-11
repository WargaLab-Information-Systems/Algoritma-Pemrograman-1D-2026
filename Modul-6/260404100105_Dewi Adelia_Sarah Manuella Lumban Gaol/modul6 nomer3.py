data_pc = []

jumlah = int(input("Jumlah PC: "))

for i in range(jumlah):
    nama = input("Nama PC: ")
    status = input("Status PC: ")
    ram = input("RAM: ")

    data_pc.append([nama, status, ram])

def cek_pc(pc):
    if pc[1] == "normal" and int(pc[2]) >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

print("Hasil Evaluasi:")

for pc in data_pc:
    if pc[2].isdigit() :
        hasil = cek_pc(pc)
    else:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')
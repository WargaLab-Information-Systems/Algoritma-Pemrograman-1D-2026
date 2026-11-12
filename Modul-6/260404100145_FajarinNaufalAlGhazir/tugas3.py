def cekLayak(status, ram):
    ramAngka = int(ram)

    if status == "normal":
        if ramAngka >= 8:
            hasil = "Layak"
        else:
            hasil = "Tidak Layak"
    else:
        hasil = "Tidak Layak"

    return hasil


inventory = []
jumlah = int(input("Jumlah PC: "))

for i in range(jumlah):
    if (i+1) == 1:
        nama = input("Nama PC pertama: ")
    else:
        nama = input(f"Nama PC ke-{i+1}: ")

    status = input("Status (Normal/Rusak): ").lower()
    ram = input("Kapasitas RAM (GB): ")
    print("-" * 30)

    satuPc = [nama, status, ram]
    inventory.append(satuPc)

for i in inventory:
    nama = i[0]
    status = i[1]
    ram = i[2]

    try:
        hasil = cekLayak(status, ram)
    except ValueError:
        hasil = "Format RAM Kacaw"

    # print('{ "PC": "' + nama + '", "Status": "' + hasil + '" }')
    print(f"PC: {nama}, Status: {hasil}")
    print("-" * 30)
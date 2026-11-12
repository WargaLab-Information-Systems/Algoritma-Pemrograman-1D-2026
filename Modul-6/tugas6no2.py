asisten = []

while True:
    nama = input("Masukkan nama asisten: ")

    if nama == "cukup":
        break

    asisten.append(nama)

asisten = tuple(asisten)

tambahan = input("Masukkan asisten tambahan: ")

asisten_akhir = asisten + (tambahan,)

hari = []

while True:
    h = input("Masukkan nama hari: ")

    if h == "cukup":
        break

    hari.append(h)

hari = tuple(hari)

kecuali_nama = input("Masukkan nama asisten pengecualian: ")
kecuali_hari = input("Masukkan hari pengecualian: ")

print("Jadwal Shift:")

i = 0
while i < len(asisten_akhir):
    j = 0

    while j < len(hari):
        if asisten_akhir[i] == kecuali_nama and hari[j] == kecuali_hari:
            j += 1
            continue

        print(asisten_akhir[i], "-", hari[j])
        j += 1

    i += 1
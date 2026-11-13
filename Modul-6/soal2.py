asisten = []

while True:
    nama = input("Masukkan nama asisten (cukup untuk selesai): ")
    if nama == "cukup":
        break
    else:
        asisten.append(nama)

asisten = tuple(asisten)

tambahan = input("Masukkan nama asisten tambahan: ")

asisten_akhir = asisten + (tambahan,)

hari = []

while True:
    h = input("Masukkan hari tugas (cukup untuk selesai): ")
    if h == "cukup":
        break
    else:
        hari.append(h)

hari = tuple(hari)

pengecualian = input("Nama asisten yang dikecualikan: ")
hari_libur = input("Hari pengecualian: ")

for a in asisten_akhir:
    for h in hari:
        if a == pengecualian and h == hari_libur:
            continue

        print(a, "-", h)
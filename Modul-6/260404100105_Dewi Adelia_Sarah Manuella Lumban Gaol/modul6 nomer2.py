asisten = []
while True:
    nama = input("Nama asisten (cukup untuk berhenti): ")

    if nama == "cukup":
        break

    asisten.append(nama)
asisten = tuple(asisten)

tambahan = input("Asisten tambahan: ")
asisten = asisten + (tambahan)

hari = []
while True:
    h = input("Nama hari (cukup untuk berhenti): ")

    if h == "cukup":
        break
    hari.append(h)
hari = tuple(hari)

kecuali_nama = input("Asisten yang dikecualikan: ")
kecuali_hari = input("Hari yang dikecualikan: ")

print("Jadwal Shift:")

for nama in asisten:
    for h in hari:
        if nama == kecuali_nama and h == kecuali_hari:
            continue
        
        print(nama, "-", h)
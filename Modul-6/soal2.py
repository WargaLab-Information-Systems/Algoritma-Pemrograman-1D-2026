asisten = []
while True:
    nama = input("Nama asisten awal (ketik 'cukup' untuk berhenti): ")
    if nama == "cukup":
        break
    asisten.append(nama)
asisten = tuple(asisten)

tambahan = input("Nama asisten tambahan: ")
asisten_akhir = asisten + (tambahan,)

hari = []
while True:
    h = input("Nama hari tugas (ketik 'cukup' untuk berhenti): ")
    if h == "cukup":
        break
    hari.append(h)
hari = tuple(hari)

ex_asisten = input("Nama asisten pengecualian: ")
ex_hari = input("Hari pengecualian: ")

print("\nJadwal shift:")
for a in asisten_akhir:
    for h in hari:
        if a == ex_asisten and h == ex_hari:
            continue
        print(f"{a} - {h}")

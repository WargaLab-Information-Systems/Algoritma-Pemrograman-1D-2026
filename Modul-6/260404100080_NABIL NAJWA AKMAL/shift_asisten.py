sementara = []
nama = input("Masukkan nama asisten awal (ketik cukup untuk berhenti): ")
while nama != "cukup":
    sementara.append(nama)
    nama = input("Masukkan nama asisten awal (ketik cukup untuk berhenti): ")
asisten_awal = tuple(sementara)

tambahan = input("Masukkan nama asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)

sementara = []
hari = input("Masukkan hari tugas (ketik cukup untuk berhenti): ")
while hari != "cukup":
    sementara.append(hari)
    hari = input("Masukkan hari tugas (ketik cukup untuk berhenti): ")
hari_tugas = tuple(sementara)

asisten_libur = input("Masukkan nama asisten pengecualian: ")
hari_libur = input("Masukkan hari pengecualian: ")

print("Kombinasi shift:")
for asisten in asisten_akhir:
    for hari in hari_tugas:
        if asisten == asisten_libur and hari == hari_libur:
            continue
        print(asisten, "-", hari)

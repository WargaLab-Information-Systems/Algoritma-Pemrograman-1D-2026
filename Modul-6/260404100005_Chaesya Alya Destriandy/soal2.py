asisten = []

nama = input("Masukkan nama asisten (cukup untuk berhenti): ")

while nama != "cukup":
    asisten.append(nama)
    nama = input("Masukkan nama asisten (cukup untuk berhenti): ")

asisten = tuple(asisten)

tambahan = input("Masukkan nama asisten tambahan: ")
asisten = asisten + (tambahan,) 


hari = []

nama_hari = input("Masukkan hari tugas (cukup untuk berhenti): ")

while nama_hari != "cukup":
    hari.append(nama_hari)
    nama_hari = input("Masukkan hari tugas (cukup untuk berhenti): ")

hari = tuple(hari)

pengecualian_nama = input("Nama asisten pengecualian: ")
pengecualian_hari = input("Hari pengecualian: ")

print("Daftar Jadwal Shift:")

for nama in asisten:
    for h in hari:
        if nama == pengecualian_nama and h == pengecualian_hari:
            continue
        print(nama, "-", h)
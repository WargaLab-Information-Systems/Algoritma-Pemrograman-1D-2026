
asisten = []

while True:
    nama = input("Masukkan nama asisten (cukup untuk berhenti): ")

    if nama.lower() == "cukup":
        break

    asisten.append(nama)

# Mengunci data asisten awal
asisten_awal = tuple(asisten)

tambahan = input("Masukkan nama asisten tambahan: ")

# Menggabungkan ke dalam wadah baru
asisten_akhir = asisten_awal + (tambahan,)

hari = []
while True:
    nama_hari = input("Masukkan hari tugas (cukup untuk berhenti): ")

    if nama_hari.lower() == "cukup":
        break

    hari.append(nama_hari)

# Mengunci daftar hari
hari_tugas = tuple(hari)

pengecualian_asisten = input("Nama asisten yang dikecualikan: ")
pengecualian_hari = input("Hari yang dikecualikan: ")

print("Jadwal Shift Asisten:")

for nama in asisten_akhir:
    for hari in hari_tugas:
        if nama == pengecualian_asisten and hari == pengecualian_hari:
            continue
        print(nama, "-", hari)

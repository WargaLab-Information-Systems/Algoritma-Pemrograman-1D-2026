daftarAsisten = []

while True:
    nama = input("Masukkan nama asisten awal (ketik 'cukup' untuk selesai): ")

    if nama.lower() == "cukup":
        break

    daftarAsisten.append(nama)


asistenAwal = tuple(daftarAsisten)

asistenTambahan = input("\nMasukkan nama asisten tambahan: ")

asistenAkhir = asistenAwal + (asistenTambahan,)


daftarHari = []

while True:
    hari = input("Masukkan hari tugas (ketik 'cukup' untuk selesai): ")

    if hari.lower() == "cukup":
        break

    daftarHari.append(hari)


hariTugas = tuple(daftarHari)


namaPengecualian = input("\nMasukkan nama asisten yang mendapat pengecualian: ")
hariPengecualian = input("Masukkan hari pengecualian: ")


print("\n=== JADWAL SHIFT ASISTEN LABORATORIUM ===")

for nama in asistenAkhir:
    for hari in hariTugas:
        if nama == namaPengecualian and hari == hariPengecualian:
            continue

        print(f"Asisten: {nama} | Hari: {hari}")

anggota = []

while True:
    nama = input("Masukkan nama anggota (selesai untuk berhenti): ")

    if nama.lower() == "selesai":
        break

    anggota.append(nama)

print("Pemeriksaan Nama Anggota:")
for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "Tidak Valid")
    else:
        print(nama, "Valid")

penyusup = input("Masukkan nama yang ingin dihapus: ")

try:
    anggota.remove(penyusup)
    print("Nama berhasil dihapus.")
except ValueError:
    print("Nama tidak ditemukan dalam pendaftaran.")

print("Daftar Anggota Akhir:", anggota)

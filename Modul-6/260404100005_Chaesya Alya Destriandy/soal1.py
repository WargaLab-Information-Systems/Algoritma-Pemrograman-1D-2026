anggota = []

nama = input("Masukkan nama anggota (selesai untuk berhenti): ")

while nama != "selesai":
    if nama in anggota:
        print("Nama tidak boleh sama")
    else:
        anggota.append(nama)

    nama = input("Masukkan nama anggota (selesai untuk berhenti): ")

print("\nDaftar Nama Anggota:")

for nama in anggota:
    print(nama)

print("\nPemeriksaan Nama Anggota:")

for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus")
else:
    print("Nama", penyusup, "tidak ditemukan")

print("Daftar Anggota Setelah Penghapusan:")
print(anggota)
daftar_nama = []

nama = input("Masukkan nama (ketik selesai untuk berhenti): ")

while nama.lower() != "selesai":
    daftar_nama.append(nama)
    nama = input("Masukkan nama (ketik selesai untuk berhenti): ")

anggota_valid = []

print("Hasil pemeriksaan:")

for nama in daftar_nama:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        anggota_valid.append(nama)
        print(nama, "valid")

target = input("Masukkan nama yang ingin dihapus (yang dicurigai): ")

while target.lower() not in [nama.lower() for nama in anggota_valid]:
    print("Nama tidak ditemukan, masukkan nama yang terdaftar!")
    target = input("Masukkan nama yang ingin dihapus (yang dicurigai): ")

ditemukan = False

for nama in anggota_valid:
    if nama.lower() == target.lower():
        anggota_valid.remove(nama)
        ditemukan = True
        break

if ditemukan:
    print("Nama berhasil dihapus")

print("Daftar anggota akhir:", anggota_valid)

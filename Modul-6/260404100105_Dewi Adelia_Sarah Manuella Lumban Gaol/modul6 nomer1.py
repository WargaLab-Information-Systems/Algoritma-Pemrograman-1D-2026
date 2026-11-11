anggota = []

while True:
    nama = input("Masukkan nama (selesai untuk berhenti): ")

    if nama == "selesai":
        break

    anggota.append(nama)

print("Pemeriksaan Nama:")

for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "Tidak Valid")
    else:
        print(nama, "Valid")

hapus = input("Nama penyusup yang dihapus: ")

while hapus not in anggota:  
    hapus = input("Masukkan nama penyusup yang dihapus (nama tidak ditemukan): ")
    
if hapus in anggota:
    anggota.remove(hapus)
else:
    print("Nama tidak ditemukan")


print("Daftar Akhir:", anggota)
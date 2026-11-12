anggota = []

while True:
    nama = input("Masukkan nama anggota: ")
    
    if nama == "selesai":
        break

    anggota.append(nama)
print("Hasil Pemeriksaan:")
i = 0
while i < len(anggota):
    if anggota[i] == "admin" or len(anggota[i]) < 4:
        print(anggota[i], "tidak valid")
    else:
        print(anggota[i], "valid")
    i += 1

hapus = input("Masukkan nama yang ingin dihapus: ")

if hapus in anggota:
    anggota.remove(hapus)
    print("Nama berhasil dihapus")
else:
    print("Nama tidak ditemukan")

print("Daftar anggota terakhir:", anggota)
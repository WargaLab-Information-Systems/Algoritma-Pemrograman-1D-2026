nama = []

while True:
    data = input("Masukkan nama (ketik selesai): ")

    if data == "selesai":
        break
    else:
        nama.append(data)

for x in nama:
    if x == "admin" or len(x) < 4:
        print(x, "tidak valid")
    else:
        print(x, "valid")

hapus = input("Masukkan nama penyusup yang ingin dihapus: ")

if hapus in nama:
    nama.remove(hapus)
    print("Nama berhasil dihapus")
else:
    print("Nama tidak ditemukan")

print("Daftar nama:", nama) 
anggota = []
while True:
    nama = input("Masukkan nama anggota (ketik 'selesai' untuk berhenti): ")
    if nama.lower() == 'selesai':
        break
    anggota.append(nama)
    
valid = []
for nama in anggota:
    if len(nama) == 4 or len(nama) == 8:
        print("Nama", nama, "diterima.")
    else:
        print("Nama", nama, "tidak valid!")
        valid.append(nama)
    anggota = valid

hapus = input ("\nMasukkan nama anggota yang dicurigai sebagai penyusup: ")

if hapus in anggota:
    anggota.remove(hapus)
    print("Nama", hapus, "telah dihapus dari daftar anggota")
else:
    print("Nama", hapus, "tidak ditemukan dalam daftar anggota")
    
print("Daftar anggota yang tersisa:")
for nama in anggota:
    print(nama)
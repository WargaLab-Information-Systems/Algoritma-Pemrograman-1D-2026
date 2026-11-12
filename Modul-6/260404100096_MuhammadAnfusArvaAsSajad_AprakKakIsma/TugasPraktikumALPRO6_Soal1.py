daftarAnggota = []

while True:
    nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk mengakhiri): ")

    if nama.lower() == "selesai":
        break

    daftarAnggota.append(nama)


print("\n=== HASIL PEMERIKSAAN NAMA ===")

for nama in daftarAnggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(f"Nama '{nama}' tidak valid.")
    else:
        print(f"Nama '{nama}' valid.")


namaPenyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")

if namaPenyusup in daftarAnggota:
    daftarAnggota.remove(namaPenyusup)
    print(f"Nama '{namaPenyusup}' berhasil dihapus.")
else:
    print(f"Nama '{namaPenyusup}' tidak ditemukan dalam pendaftaran.")


print("\n=== DAFTAR ANGGOTA AKHIR ===")

for nama in daftarAnggota:
    print(nama)
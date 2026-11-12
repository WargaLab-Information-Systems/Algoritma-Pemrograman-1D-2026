daftar = []
nama = input("Masukkan nama calon anggota (ketik selesai untuk berhenti): ")
while nama != "selesai":
    daftar.append(nama)
    nama = input("Masukkan nama calon anggota (ketik selesai untuk berhenti): ")

for calon in daftar:
    if calon == "admin" or len(calon) < 4:
        print(calon, "tidak valid")

penyusup = input("Masukkan nama penyusup yang ingin dihapus: ")
if penyusup in daftar:
    daftar.remove(penyusup)
    print(penyusup, "berhasil dihapus")
else:
    print(penyusup, "tidak ada di pendaftaran")

print("Daftar anggota sekarang:", daftar)

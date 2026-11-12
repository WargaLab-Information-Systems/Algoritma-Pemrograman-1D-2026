daftar = []
while True:
    nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti)")
    if nama == "selesai":
        break
    daftar.append(nama)

print("Evaluasi")
for namna in daftar:
    if nama == "admin" or len(nama) < 4:
        print(f"{nama}: nama tidak valid")

penyusup = input(" Masukkan Nama penyusup yang mau dihapus")
try:
    daftar.remove(penyusup)
    print(f"{penyusup}Berhasil dihapus")
except ValueError:
    print(f"{penyusup} tidak dietmukan di daftar pendaftaran")

print("Daftar akhir:", daftar)


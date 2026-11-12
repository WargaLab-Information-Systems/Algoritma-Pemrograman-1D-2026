nama = []

while True:
    namaUser = input("Masukkan nama calon anggota baru ('selesai' untuk berhenti): ")
    if namaUser == "selesai":
        break
    else:
        nama.append(namaUser)

valid = True
print("-" * 30)
for i in nama:
    if i == "admin" or len(i) < 4:
        valid = False
        print(f"Nama {i} tidak valid, nama telah dihapus dari daftar :(")
        nama.remove(i)

print("-" * 30)
print(f"Daftar nama calon anggota baru: {nama}")

print("-" * 30)
while True:
    penyusup = input("Masukkan nama penyusup ('selesai' untuk berhenti): ")
    if penyusup == "selesai":
        break
    try:
        nama.remove(penyusup)
        print(f"{penyusup} telah dihapus dari daftar")
    except ValueError:
        print(f"{penyusup} tidak ditemukan dalam daftar")

print("-" * 30)
if nama == []:
    print("Daftar nama calon anggota baru kosong")
else:
    print(f"Daftar nama calon anggota baru: {nama}")
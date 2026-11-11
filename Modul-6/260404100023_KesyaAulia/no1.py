calon_anggota = []
yang_tidaksesuai = []

while True:
    nama = input("masukkan nama anggota :")
    if nama == "selesai":
        break

    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
        yang_tidaksesuai.append(nama)
    else:
        print(nama, "valid")
        calon_anggota.append(nama)

# for nama in calon_anggota:
#     if nama == "admin" or len(nama) < 4:
#         print(nama, "tidak valid")
#         # yang_tidaksesuai.append(nama)
#     else:
#         print(nama, "valid")

# if nama == "admin" and len(nama) < 4:
#     calon_anggota.remove(nama)


hapus_nama = input("masukkan nama yang akan di hapus: ")

if hapus_nama in calon_anggota:
    calon_anggota.remove(hapus_nama)
else:
    print(hapus_nama, "tidak ada di list calon anggota")
print("calon anggota saat ini adalah: ", calon_anggota)

    
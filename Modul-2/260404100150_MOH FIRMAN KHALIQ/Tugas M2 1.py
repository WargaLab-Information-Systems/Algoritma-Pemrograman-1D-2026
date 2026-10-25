kode = int(input("Masukkan kode rahasia 3 digit: "))


digit1 = kode // 100
digit2 = (kode // 10) % 10
digit3 = kode % 10


pelacak_awal = digit1 * digit3


if digit2 % 2 == 1:
    pelacak_tahap1 = pelacak_awal + 25
else:
    pelacak_tahap1 = pelacak_awal - digit2


if pelacak_tahap1 % 3 == 0:
    nilai_akhir = pelacak_tahap1 // 3
else:
    nilai_akhir = pelacak_tahap1 * 2


if nilai_akhir > 50:
    status = "Kategori A"
elif nilai_akhir > 20:
    status = "Kategori B"
else:
    status = "Password Ditolak"


if nilai_akhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"


print("HASIL VALIDASI PASSWORD")
print("Digit pertama :", int(digit1))
print("Digit kedua   :", int(digit2))
print("Digit ketiga  :", int(digit3))
print("Pelacak awal  :", int(pelacak_awal))
print("Tahap pertama :", int(pelacak_tahap1))
print("Tahap kedua   :", int(nilai_akhir))
print("Status        :", status)
print("Siklus        :", siklus)
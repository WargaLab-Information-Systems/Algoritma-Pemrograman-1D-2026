password = int(input("Masukkan 3 digit password: "))

digit_1 = password // 100
digit_2 = (password // 10) % 10
digit_3 = password % 10

pelacak = digit_1 * digit_3
pelacak_awal = pelacak


if digit_2 % 2 == 0: 
    pelacak -= digit_2
else:               
    pelacak += 25
pelacak_tahap1 = pelacak


if pelacak % 3 == 0:
    pelacak //= 3
else:
    pelacak *= 2
nilai_akhir = pelacak


if nilai_akhir > 50:
    status = "Kategori A"
elif nilai_akhir > 20:
    status = "Kategori B"
else:
    status = "Password Ditolak"


siklus = "Siklus Genap" if nilai_akhir % 2 == 0 else "Siklus Ganjil"

print("Digit: ", digit_1, digit_2, digit_3)
print("Nilai Pelacak Awal:", pelacak_awal)
print("Setelah Tahap 1:", pelacak_tahap1)
print("Nilai Akhir Tahap 2:", nilai_akhir)
print("Status Password:", status)
print(f"Siklus: {siklus}" )
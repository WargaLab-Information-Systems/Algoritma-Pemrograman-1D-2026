password = int(input("Masukkan password 3 digit: "))

digit1 = password // 100
digit2 = (password // 10) % 10
digit3 = password % 10

pelacak = digit1 * digit3

if digit2 % 2 == 0:
    pelacak = pelacak - digit2
else:
    pelacak = pelacak + 25

if pelacak % 3 == 0:
    pelacak = pelacak / 3
else:
    pelacak = pelacak * 2

if pelacak > 50:
    kategori = "Kategori A"
elif pelacak > 20:
    kategori = "Kategori B"
else:
    kategori = "Password Ditolak"

if pelacak % 2 == 0:
    status = "Genap"
else:
    status = "Ganjil"

print("Nilai Pelacak:", pelacak)
print("Kategori:", kategori)
print("Status:", status)
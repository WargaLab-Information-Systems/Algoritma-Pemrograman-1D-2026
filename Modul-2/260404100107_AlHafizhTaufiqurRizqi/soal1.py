digit1 = int(input("Masukkan digit 1: "))
digit2 = int(input("Masukkan digit 2: "))
digit3 = int(input("Masukkan digit 3: "))

nipel = digit1 * digit3

if digit2 % 2 == 0:
    np1 = nipel - digit2
else:
    np1 = nipel + 25

if np1 % 3 == 0:
    np2 = nipel / 3
else:
    np2 = nipel * 2

if np2 > 50:
    kategori = "Kategori A"
elif np2 > 20:
    kategori = "Kategori B"
else:
    kategori = "password ditolak"

if np2 % 2 == 0:
    siklus = "siklus genap"
else:
    siklus = "siklus ganjil"

print("digit2 =", digit2)
print("digit3 =", digit3)
print("nipel =", nipel)
print("np1 =", np1)
print("np2 =", np2)
print("kategori =", kategori)
print("siklus =", siklus)
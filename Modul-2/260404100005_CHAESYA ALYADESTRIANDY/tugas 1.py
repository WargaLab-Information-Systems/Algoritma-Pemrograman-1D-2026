password = int(input("Masukkan password 3 digit: "))

# Memisahkan digit
digit1 = (password - password % 100) // 100
digit2 = (password % 100 - password % 10) // 10
digit3 = password % 10

# Nilai pelacak awal
nilai_pelacak_awal = digit1 * digit3

# Perubahan tahap pelacak awal
if digit2 % 2 == 1:
    nilai_pelacak = nilai_pelacak_awal + 25
else:
    nilai_pelacak = nilai_pelacak_awal - digit2

# Perubahan tahap kedua / kelipatan 3
if nilai_pelacak % 3 == 0:
    nilai_pelacak_akhir = nilai_pelacak // 3
else:
    nilai_pelacak_akhir = nilai_pelacak * 2

# Menentukan status password
if nilai_pelacak_akhir > 50:
    status_password = "Kategori A"
elif nilai_pelacak_akhir > 20:
    status_password = "Kategori B"
else:
    status_password = "Password Ditolak"

# Menentukan siklus
if nilai_pelacak_akhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"

# Output
print("Digit pertama :", digit1)
print("Digit kedua   :", digit2)
print("Digit ketiga  :", digit3)
print("Nilai pelacak awal :", nilai_pelacak_awal)
print("Nilai pelacak tahap 1 :", nilai_pelacak)
print("Nilai pelacak akhir :", nilai_pelacak_akhir)
print("Status password :", status_password)
print("Siklus :", siklus)

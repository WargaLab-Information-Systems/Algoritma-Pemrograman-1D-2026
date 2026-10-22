# Input password
password = int(input("Masukkan password 3 digit: "))

# Memisahkan password menjadi 3 digit
digit1 = password // 100
digit2 = (password // 10) % 10
digit3 = password % 10

print("Digit pertama :", digit1)
print("Digit kedua   :", digit2)
print("Digit ketiga  :", digit3)

# Menghitung nilai pelacak awal
nilai_pelacak_awal = digit1 * digit3

# Perubahan tahap pertama
if digit2 % 2 != 0:
    nilai_pelacak = nilai_pelacak_awal + 25
else:
    nilai_pelacak = nilai_pelacak_awal - digit2

# Perubahan tahap kedua
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

if nilai_pelacak_akhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"

print("Digit pertama            :", digit1)
print("Digit kedua              :", digit2)
print("Digit ketiga             :", digit3)
print("Nilai pelacak awal       :", nilai_pelacak_awal)
print("Nilai pelacak tahap 1    :", nilai_pelacak)
print("Nilai pelacak tahap 2    :", nilai_pelacak_akhir)
print("Status password          :", status_password)
print("Siklus                   :", siklus)
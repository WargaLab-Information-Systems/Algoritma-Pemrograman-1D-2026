password = int(input("Masukkan password: "))

digit1 = (password - password % 100) / 100
digit2 = (password % 100 - password % 10) / 10
digit3 = password % 10

nilai_pelacak_awal = digit1 * digit3

if digit2 % 2 == 0:
    nilai_pelacak = nilai_pelacak_awal - digit2
else:
    nilai_pelacak = nilai_pelacak_awal + 25

if nilai_pelacak % 3 == 0:
    nilai_pelacak_akhir = nilai_pelacak / 3
else:
    nilai_pelacak_akhir = nilai_pelacak * 2

if nilai_pelacak_akhir > 50:
    status_password = "kategori A"
else:
    if nilai_pelacak_akhir > 20:
        status_password = "kategori B"
    else:
        status_password = "password di tolak"

if nilai_pelacak_akhir % 2 == 0:
    siklus = "siklus genap"
else:
    siklus = "siklus ganjil"

print("digit pertama :", digit1)
print("digit kedua :", digit2)
print("digit ketiga :", digit3)
print("nilai pelacak awal :", nilai_pelacak_awal)
print("nilai pelacak tahap 1 :", nilai_pelacak)
print("nilai pelacak akhir :", nilai_pelacak_akhir)
print("status password :", status_password)
print("siklus :", siklus)
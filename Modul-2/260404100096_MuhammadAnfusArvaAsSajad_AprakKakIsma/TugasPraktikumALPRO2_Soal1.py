password = int(input("Masukkan password 3 digit: "))

digit1 = password // 100
digit2 = (password % 100) // 10
digit3 = password % 10

print("Digit pertama:", digit1)
print("Digit kedua:", digit2)
print("Digit ketiga:", digit3)

pelacakAwal = digit1 * digit3
print("Nilai pelacak awal:", pelacakAwal)

if digit2 % 2 == 1:
    pelacakTahap1 = pelacakAwal + 25
else:
    pelacakTahap1 = pelacakAwal - digit2

print("Nilai pelacak tahap 1:", pelacakTahap1)

if pelacakTahap1 % 3 == 0:
    nilaiAkhir = pelacakTahap1 // 3
else:
    nilaiAkhir = pelacakTahap1 * 2

print("Nilai pelacak tahap 2:", nilaiAkhir)

if nilaiAkhir > 50:
    status = "Kategori A"
elif nilaiAkhir > 20:
    status = "Kategori B"
else:
    status = "Password Ditolak"

print("Status Password:", status)

if nilaiAkhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"

print(siklus)
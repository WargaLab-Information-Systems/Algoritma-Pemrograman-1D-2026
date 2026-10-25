pw = int(input("masukkan pasword 3 digit:"))
digit1 = pw // 100
digit2 = (pw // 10) % 10
digit3 = pw % 10

print("digit pertama:", digit1)
print("digit kedua:", digit2)
print("digit ketiga: ", digit3)

pertama = digit1 * digit2

if digit2 % 2 == 1:
    lanjut = pertama - digit2
else:
    lanjut = pertama + 25 

if lanjut % 3 == 0:
    next = lanjut / 3
else:
    next = lanjut * 3

if next > 50:
    print("Kategori A")
elif next > 20:
    print("kategori B")
else:
    print("pasword salah")

if next % 2 == 0:
    print("siklus genap")
else:
    print("siklus ganjil")
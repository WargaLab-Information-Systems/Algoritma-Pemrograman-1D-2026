a = int(input("digit pertama: "))
b = int(input("digit ke dua: "))
c = int(input("digit ke tiga: "))

pelacak = a * c
print("nilai pelacak awal:",pelacak)

if b % 2 == 1:
    pelacak += 25
else:
    pelacak -= b

print("setelah tahap 1:",pelacak)

if pelacak % 3 == 0:
    pelacak //= 3

else:
    pelacak *= 2

print("nilai akhir:",pelacak)

if pelacak > 50:
    status = "Kategori A"
elif pelacak > 20:
    status = "Kategori B"
else:
    status = "Password Ditolak"

siklus = "Siklus Genap" if pelacak % 2 == 0 else "Siklus Ganjil"

print("Status Password:", status)
print(siklus)

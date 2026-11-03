password = int(input("Masukkan Password 3 digit: "))

digit1 = (password - (password % 100)) / 100; 
digit2 = ((password - (password % 10)) / 10) % 10;
digit3 = password % 10

np = digit1 * digit3

if digit2 % 2 == 0:
    np1 = np - digit2
else:
    np1 = np + 25

if np1 % 3 == 0:
    np2 = np1 // 3
else:
    np2 = np1 * 2
    
if np2 > 50:
    kategori = "Kategori A"
elif np2 > 20:
    kategori = "Kategori B"
else:
    kategori = "Password Ditolak"
        
if np2 % 2 == 0:
    siklus = "Genap"
else:
    siklus = "Ganjil"

print(f"Digit anda                              : {int(digit1)}, {int(digit2)}, {int(digit3)}")
print(f"Nilai pelacak awal                      : {int(np)}")
print(f"Nilai pelacak setelah perubahan pertama : {int(np1)}")
print(f"Nilai pelacak setelah perubahan kedua   : {int(np2)}")
print(f"Status Password                         : {kategori}")
print(f"Siklus pelacak                          : {siklus}")
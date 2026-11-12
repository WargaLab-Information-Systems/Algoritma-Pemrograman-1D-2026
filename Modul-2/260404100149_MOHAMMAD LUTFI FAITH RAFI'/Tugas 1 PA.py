# digit1 = int(input("masukkan digit 1 :"))
# digit2 = int(input("masukkan digit 2 :"))
# digit3 = int(input("masukkan digit 3 :"))

kode = int(input("nilai digit: "))

digit1 = kode // 100
digit2 = kode // 10 % 10
digit3 = kode % 10 


nilai_pelacak = digit1 * digit3
if digit2 % 2 == 0:
    nilai_tahap1 = nilai_pelacak - digit2
else:
    nilai_tahap1 = nilai_pelacak + 25
print("nilai pelacak setelah tahap pertama =", nilai_tahap1)

if nilai_pelacak % 3 == 0:
    nilai_tahap2 = nilai_pelacak // 3 
else:
    nilai_tahap2 = nilai_pelacak * 2
print("nilai pelacak tahap kedua =", nilai_tahap2)
    
if nilai_pelacak >= 50:
    print("Status = kategori A")
elif nilai_pelacak >= 20:
    print("status = kategori B") 
else:
    print("status = password ditolak")

siklus = "genap" if nilai_pelacak % 2 == 0 else "ganjil"
print(siklus)


    


    






# Input total belanja 
total = int(input("masukkan total belanja : Rp"))
# Menentukan diskon
if total % 100000 == 0: 
    bayar = 0 
elif total % 50000 == 0:
    bayar = total * 50 / 100
elif total % 10000 == 0 : 
    bayar = total * 80 / 100
elif total > 200000 :
    bayar = total * 90 / 100
else : 
    bayar = total
#menampilkan total awal 
print ("total belanja awal : Rp", total)
#Menampilkan total yang harus dibayar 
print("total harga akhir : Rp",bayar)
#Ternary operator untuk poin
poin = "poin bertambah" if bayar > 0 else "tidak ada point"

print ("Status poin :",poin)
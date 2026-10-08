total = int(input("masukkan total belanja awal ="))
print("Total belanja awal =", total)

if total % 100000 == 0:
    diskon = 100
elif total % 50000 == 0:
    diskon = 50
elif total % 10000 == 0:
    diskon = 20
elif total >= 200000: 
    diskon = 10
else:
    diskon = 0

print("presentase diskon:", diskon, "%") 

nilai_diskon = int(total * diskon / 100)
print("nilai diskon: Rp", nilai_diskon)

total_bayar = total - nilai_diskon
print("total yang harus dibayar: Rp", total_bayar)

status_poin = "poin bertambah" if total_bayar > 0 else "tidak ada poin"
print("status poin: ", status_poin)










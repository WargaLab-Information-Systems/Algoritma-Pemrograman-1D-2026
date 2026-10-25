nama_kop= "KOPERASI NDESO"
print(nama_kop)
belanja= int (input("masukkan total belanjaan:"))
if belanja >= 200000 :
     diskon=belanja * 10/100
     total_diskon= belanja - diskon
     print("diskon 10%",total_diskon)
elif belanja% 100000==0:
     diskon= belanja * 100/100
     total_diskon= int (belanja - diskon)
     print("harga belanjaan diskon 100% =",total_diskon)
elif belanja % 50000==0:
     diskon=belanja * 50/100
     total_diskon= int(belanja - diskon)
     print("harga belanjaan diskon 50% =",total_diskon)
elif belanja % 10000==0:
     diskon=belanja * 20/100
     total_diskon= belanja - diskon
     print("harga belanjaan diskon 20%=",total_diskon)
else:
     total_diskon=belanja
     print("harga normal=",total_diskon)

status = "poin bertambah" if total_diskon > 0  else "tidak ada poin"
print(status)
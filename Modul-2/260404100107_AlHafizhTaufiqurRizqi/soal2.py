belanja = int(input("Masukkan total belanja: Rp"))

harga_awal = belanja

if belanja % 100000 == 0:
    diskon = 100
elif belanja % 50000 == 0:
    diskon = 50
elif belanja % 10000 == 0:
    diskon = 20
elif belanja >= 200000:
    diskon = 10
else:
    diskon = 0

potongan = belanja * diskon / 100
harga_akhir = belanja - potongan

print("Total belanja awal : Rp", belanja)
print("Diskon             :", diskon, "%")
print("Potongan            : Rp", potongan)
print("Total yang dibayar  : Rp", harga_akhir)

status = "poin bertambah" if belanja < 0 else "tidak ada poin"
print("status;", status)
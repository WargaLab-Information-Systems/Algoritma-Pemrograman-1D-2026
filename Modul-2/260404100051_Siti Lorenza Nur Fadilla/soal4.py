pin = int(input("Masukkan PIN 3 digit: "))
jam = float(input("Masukkan jam kedatangan (0-23): "))

d1 = pin // 100
d2 = (pin // 10) % 10
d3 = pin % 10

print("Digit pertama :", d1)
print("Digit kedua   :", d2)
print("Digit ketiga  :", d3)

if pin % 5 == 0:
    if jam < 12:
        print("Garasi Pagi Terbuka")
    else:
        print("Garasi Malam Terbuka, Lampu Dinyalakan")

elif pin % 2 == 0:
    if d1 + d3 == d2:
        print("Garasi VIP Terbuka Khusus Bos")
    else:
        print("Kode Genap Ditolak, Alarm Berbunyi!")

else:
    print("Akses Ditolak")

cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("Status CCTV :", cctv)
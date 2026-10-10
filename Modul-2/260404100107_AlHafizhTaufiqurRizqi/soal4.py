pin = int(input("Masukkan PIN 3 digit: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

print("\nDigit pertama :", digit1)
print("Digit kedua   :", digit2)
print("Digit ketiga  :", digit3)

if pin % 5 == 0:
    if jam < 12:
        print("Garasi Pagi Terbuka")
    else:
        print("Garasi Malam Terbuka, Lampu Dinyalakan")

elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        print("Garasi VIP Terbuka Khusus Bos")
    else:
        print("Kode Gagal Ditolak, Alarm Berbunyi")

else:
    print("Akses Ditolak Sepenuhnya")

cctv = "Mode Malam Menyala" if jam > 18 else "Mode Siang Standby"

print("Status CCTV:", cctv)
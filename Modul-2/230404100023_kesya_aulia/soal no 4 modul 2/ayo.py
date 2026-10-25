pin = int(input("masukkan PIN 3 digit: "))
jam = float(input("masukkan jam ked"))

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

print("angka digit pertama: ", digit1)
print("angka digit kedua: ", digit2)
print("angka digit ketiga: ", digit3)

if pin % 5 == 0:
    if jam < 12:
        print("garasi pagi terbuka")
    if jam >= 12:
        print("garasi malam terbuka, lampu dinyalakan")
if pin % 5 != 0:
    if pin % 2 == 0:
        if digit1 + digit3 == digit2:
            print("garansi VIP terbuka kusus bos")
        else:
            print("kode genap ditolak, alarm berbunyi")
    else:
        print("akses di tolak")

status_kamera = "mode malam merekam" if jam > 18 else "mode siang stanby"
print(status_kamera)
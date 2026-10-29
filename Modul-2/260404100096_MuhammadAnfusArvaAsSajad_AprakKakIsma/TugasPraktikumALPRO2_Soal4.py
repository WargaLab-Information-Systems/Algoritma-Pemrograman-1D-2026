pin = int(input("Masukkan PIN 3 digit: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

digit1 = pin // 100
digit2 = (pin % 100) // 10
digit3 = pin % 10

print("Digit pertama:", digit1)
print("Digit kedua:", digit2)
print("Digit ketiga:", digit3)

if pin % 5 == 0:
    if jam < 12:
        status = "Garasi Pagi Terbuka"
    else:
        status = "Garasi Malam Terbuka, Lampu Dinyalakan"

elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        status = "Garasi VIP Terbuka Khusus CEO yang menyamar"
    else:
        status = "Kode Genap Ditolak, CEO palsu terdeteksi! Alarm Berbunyi!"

else:
    status = "Akses Ditolak"

print("Status akses:", status)

cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("Status CCTV:", cctv)
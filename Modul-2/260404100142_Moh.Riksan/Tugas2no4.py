pin = int(input("Masukkan PIN Garasi (3 digit): "))
jam = int(input("Masukkan jam saat ini (0-23): "))
digit1 = pin // 100
digit2 = (pin //10) % 10
digit3 = pin % 10

# Menentukan status akses pintu garasi
if pin % 5 == 0:
    if jam < 12:
        pesan = "Garasi Pagi Terbuka"
    else:
        pesan = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        pesan = "Garasi VIP Terbuka Khusus Bos"
    else:
        pesan = "Kode Genap Ditolak, Alarm Berbunyi!"

# Ternary operator untuk status CCTV
cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

# Tampilkan hasil
print("Digit pertama :", digit1)
print("Digit kedua   :", digit2)
print("Digit ketiga  :", digit3)
print("Status akses  :", pesan)
print("Status CCTV   :", cctv)
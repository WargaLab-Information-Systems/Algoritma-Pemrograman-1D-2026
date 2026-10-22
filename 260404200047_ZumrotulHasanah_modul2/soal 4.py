# Input PIN dan jam kedatangan
pin = int(input("Masukkan PIN 3 digit: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

# Memisahkan digit PIN
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

# Menampilkan digit PIN
print("Digit pertama :", digit1)
print("Digit kedua   :", digit2)
print("Digit ketiga  :", digit3)

# Menentukan akses garasi
if pin % 5 == 0:

    if jam < 12:
        status = "Garasi Pagi Terbuka"
    else:
        status = "Garasi Malam Terbuka, Lampu Dinyalakan"

elif pin % 2 == 0:

    if digit1 + digit3 == digit2:
        status = "Garasi VIP Terbuka Khusus Bos"
    else:
        status = "Kode Genap Ditolak, Alarm Berbunyi!"

else:
    status = "Akses Ditolak"

# Menampilkan status akses
print("Status Akses :", status)

# Ternary operator untuk CCTV
cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("Status CCTV :", cctv)
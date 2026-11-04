pin = int(input("Masukkan PIN 3 digit: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

# Mengambil setiap digit PIN secara matematis
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

print("--- HASIL PEMERIKSAAN ---")
print("Digit pertama :", digit1)
print("Digit kedua   :", digit2)
print("Digit ketiga  :", digit3)

# Pemeriksaan PIN
if pin % 5 == 0:
    # PIN merupakan kelipatan 5

    if jam < 12:
        print("Garasi Pagi Terbuka")
        print("Lampu: Mati")
    else:
        print("Garasi Malam Terbuka")
        print("Lampu: Menyala")

elif digit1 % 2 == 0 and digit2 % 2 == 0 and digit3 % 2 == 0:
    # Semua digit PIN merupakan angka genap

    if digit1 + digit3 == digit2:
        print("Garasi VIP Terbuka Khusus Bos")
    else:
        print("Kode Genap Ditolak")
        print("Alarm Berbunyi")

else:
    print("Akses Ditolak Sepenuhnya")


# Status kamera CCTV menggunakan ternary operator
status_kamera = "Mode Malam Merekam" if jam >= 18 else "Standby"

print("Status Kamera CCTV:", status_kamera)
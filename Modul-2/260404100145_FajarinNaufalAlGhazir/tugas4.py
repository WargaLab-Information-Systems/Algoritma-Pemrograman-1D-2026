pin = int(input("Masukkan PIN 3 digit: "))
jamDatang = int(input("Jam Kedatangan (dalam format 0-23): "))

digit1 = (pin - (pin % 100)) / 100; 
digit2 = ((pin - (pin % 10)) / 10) % 10;
digit3 = pin % 10

if pin % 5 == 0:
    if jamDatang < 12:
        pesan = "Garasi Pagi Terbuka"
    else:
        pesan = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if (digit1 + digit3) == digit2:
        pesan = "Garasi VIP Terbuka Khusus Bos"
    else:
        pesan = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    pesan = "Akses DITOLAK"
    
print(f"PIN                : {int(digit1)}, {int(digit2)}, {int(digit3)}")
print(f"Pesan Akses Pintu  : {pesan}")
print("Mode Malam Merekam") if jamDatang > 18 else print("Mode Siang Standby")

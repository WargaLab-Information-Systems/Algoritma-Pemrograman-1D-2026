pin = int(input("Masukkan 3 digit PIN: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))


d1 = pin // 100
d2 = (pin // 10) % 10
d3 = pin % 10


if pin % 5 == 0:
    if jam < 12:
        pesan_akses = "Garasi Pagi Terbuka"
    else:
        pesan_akses = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if (d1 + d3) == d2:
        pesan_akses = "Garasi VIP Terbuka Khusus Bos"
    else:
        pesan_akses = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    pesan_akses = "Akses Ditolak Sepenuhnya"


status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("Digit PIN::", d1, d2, d3)
print("Status Akses:", pesan_akses)
print("Status CCTV:", status_cctv)
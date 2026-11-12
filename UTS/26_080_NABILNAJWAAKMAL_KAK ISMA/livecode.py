Regular = 40000
VIP = 75000
VVIP = 100000

tiket_regular = 0
tiket_vip = 0
tiket_vvip = 0
for i in range (10):
    tipe_tiket = int(input("masukkan harga tiket yg ingin anda beli (Reguler 40000) (VIP 75000) (VVIP 100000) JIKA INGIN MENGAKHIRI PROGRAM MAKA TULIS 0 :"))
    if tipe_tiket == Regular:
        tiket_regular += 1
    elif tipe_tiket == VIP:
        tiket_vip += 1
    elif tipe_tiket == VVIP:
        tiket_vvip += 1
    else:
        break

if tiket_regular > 0:
    minuman  = str(input("kami menawarkan minuman, apakah ingin membeli?? (Y/N) :"))
    if minuman == "Y" or minuman == "y":
        print("anda membeli minuman")
    else:
        print("anda tidak membeli minuman")
elif tiket_vip > 0 or tiket_vvip > 0:
    print("anda mendapatkan minuman")
else:
    pass


# untuk variablenya
reguler=40000
vip=75000
vvip=100000
minuman=10000
tiket1=reguler
tiket2=vip
tiket3=vvip
# untuk memasukkan nilai tiket
while True:
    tiket = (input("masukkan tiket:"))
    if tiket == "stop" :
            break
    if tiket== tiket1:
            print("silahkan kalau mau tambah minuman harga",minuman)
            jwb=input("masukkan Y/n:")
            print(jwb)
    elif tiket==tiket2 :
         print("mendapatkan minuman gratis")
    elif tiket== tiket3:
         print("mendapatkan minuman gratis")
        
    # menghitung total
    kartu = "member card"
    if kartu >3:
          diskon = 15/100
          ttl_diskon= tiket - diskon
    else:
          print("tidak ada diskon")
    
# bagian ini untuk bagian pembayaran jika kurang akan menginput nilai lagi
    while True:
          nominal=int("masukkan nominal")
          if nominal < tiket:
                ("nominal kurang") 
          else:
                print("uang pas")

    
    
    




regular = 40.000
vip = 75.000
vvip = 100.000
tiket = 0
y = 0
konsumsi: 0
member = 0
pembelian = 0
total : 0


while True:
    tiket = input("Silahkan memilih tiket (regular, vip, vvip): ")
    pelanggan = input("apakah memiliki member card (y/n): ")
    
    if tiket == regular:
            print("apakah anda ingin menambahkan minuman seharga Rp. 10000/tiket? ")
            if y > 0:
                konsumsi = konsumsi + 1
            else:
                print("tidak menambah minuman") 
    elif tiket == vip:
        print("Mendapatkan minuman gratis setelah membeli tiket ")
    elif tiket == vvip:
        print("Mendapatkan minuman gratis setelah membeli tiket ")
        
        tiket += 1
        konsumsi += tiket
        
    elif tiket > 3:
        if tiket == pelanggan:
            member = member * 15/100
        else :
            member= member * 10/100
            
    
        
    else :
        print("belum membeli tiket")
        
    total = tiket + member
    print(total)
        

        
        
    


    
# saya menggunakan perulangan while karena didalam soal pelanggan bisa membeli lebih dari 1 dan kondisinya belum ditemukan akan diulang berapa kali
# menggunakan if-elif-else karena terdapat banyak kondisi.
# ketika pelanggan 
    
   
    
    
        
    
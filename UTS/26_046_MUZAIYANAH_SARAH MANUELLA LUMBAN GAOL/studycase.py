# TICKET ORDERING SYSTEM


pil1 = "Regular = Rp 40.000" #Memasukkan harga tiket regular
pil2 = "VIP = Rp 75.000" #Memasukkan harga tiket vip
pil3 = "VVIP = Rp 100.000" #Harga tiket vvip

print(input("Order tiket tipe apa? "))  #Untuk menanyakan kepada pelanggan membeli tiket tipe apa

while True: #Looping
    if pil1 : 
        print(input("Beli minuman seharga 10.000"))
        if "Y" :
            print("Pelanggan membeli minuman")
        else:
            print("Pelanggan tidak membeli minuman")
        continue 
    else:
        print("Anda mendapatkan minuman gratis!")




# pelanggan = 0
# print(input("Mau beli tipe tiket apa? "))

# if "Regular" :
#     print("Anda harus membayar Rp 40.000")
# elif "VIP":
#     print("Anda membayar RP75.000")
# elif "VVIP":
#     print("Anda membayar Rp100.000")
# else:
#     print("Anda tidak membeli apapun")        
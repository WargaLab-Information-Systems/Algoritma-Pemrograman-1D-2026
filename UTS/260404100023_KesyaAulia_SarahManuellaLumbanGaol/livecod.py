
reguler = int(input("masukkan julmah tiket reguler: "))
vip = int(input("masukkan jumlah tiket vip: "))
vvip = int(input("masukkan jumlah tiket :"))

card = input("apakah anda memiliki member card? jika iya masukkan angka 1, jika tidak masukkan 0")

jumlah = reguler + vip + vvip 
 

while jumlah == 0: 
    reguler = int(input("masukkan julmah tiket reguler: "))
    vip = int(input("masukkan jumlah tiket vip: "))
    vvip = int(input("masukkan jumlah tiket :"))
    jumlah = reguler + vip + vvip 

    if reguler >0:
        yn = input("Y/N")
        minuman = reguler * 10000
    if vip > 0 and vvip >0:
        print("mendapat minuman gratis ")

    uang = (reguler * 40.000 + minuman)+(vip * 75000)+(viip * 100000)
    
    if jumlah >3:
        if card == 1:
            diskon = uang * 15/100
            if card == 0:
                diskon = 0

    bayar = uang - diskon
    duit = int(input("masukkan uangmu: "))
    
    if duit < bayar:
            duit = int(input("masukkan uangmu: "))
    print("lunas")

    kembali = duit - bayar
    print("uang kembalian", kembali)

#di awal kkta meminta input berapa jumlah ytiket yang di beli, di setiap jenis tiketnya, lalu memasukkan apakah member atau tidak,
#jika member masukkan angka 1 jika tidak masukka angka 0,lalu menjumlah semua total tiketnya, terus masuk ke while, dilihat
#jika tiket itu 0 maka akan meminta inputan lagi mengenai tiket yang akan di beli, lalu menjumlahkan keseluruhan tiket
#lalu mengecek apakah tiket reguler lebih dari 0? jika iya minta inputan yn, lalu mendapat minum dimana harganya minuman persatu tiket itu 10000
#lalu jika vvip dan vip lebh dari 0 maka akan mendapat minuman gratis
#lalu menghitung total uangnya, lalu di lihat apakah jumlah keseluruhan tiket itu lebih dari 3? jika ia dan dia memiliki card maka 
#akan mendapat diskon 15% jika tidak maka tidak akan mendapat diskon, lalu menghitung uang yang akan dibayar setelah mendapat diskon
#lalu menginput uang yng di bayar
#jika uang kurang dari jumlah yang seharusnya di bayar maka akan meminta uang lagi, trs menghitung kembalian dari dari uang di kurangi jumlah yg harus di bayar

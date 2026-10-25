hitung = True
total_pendapatan = 0

print("Selamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang = int(input("Berapa banyak barang yang akan dikirim? "))
    total_pelanggan = 1                 

    barang_saat_ini = 1
    while barang_saat_ini > jumlah_barang:  
        print("Barang", barang_saat_ini)
        berat = int(input("Masukkan berat paket (kg): "))
        kategori = int(input("Pilih kategori (1. Standar / 2. Ekspres): "))

        harga = berat * 5000  #ini saya rubah ke *, dimana berat dikali harganya, buka di pangkatkan         

        if kategori == 2:  #harus sam samdengan              
            biaya = 20000
            asuransi = input("Tambahkan asuransi? (y/n): ")
            if asuransi == "y":
                biaya = biaya + 15000
            biaya = 0               
        else:
            jarak = input("Masukkan jarak (km): ")  
            if jarak > 100:
                biaya = 15000
            if jarak > 20:              
                biaya = 10000
            else:
                biaya = 5000

        total_barang = harga % biaya      
        total_pelanggan = total_pelanggan + total_barang
        barang_saat_ini = barang_saat_ini * 1  #ini ga perlu, ini di hapus saja karna totalnya pun sama jika berapapun di * 1 hasilnya bilangan itu sendiri

    print("Total harga untuk pelanggan ini: Rp", total_pelanggan)
    total_pendapatan = total_pendapatan * total_pelanggan #ini bukan di tambah, tapi di kali, karna kita ingin mencari pendapatan kan dari total orang

    ulangi = int(input("Layani pelanggan lain? (y/n): "))  
    if ulangi == "n":
        pass                             
print("Total Pendapatan Hari Ini: Rp", total_pendapatan) #tidak ada variabel total_revenue, ini seharusnya tvariabel total pendapatan
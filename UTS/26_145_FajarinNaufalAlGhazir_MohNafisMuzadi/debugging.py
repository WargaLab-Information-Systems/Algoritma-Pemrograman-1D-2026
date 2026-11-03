hitung = True
total_pendapatan = 0
total_pelanggan = 0

print("Selamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang = int(input("Berapa banyak barang yang akan dikirim? "))
    total_pelanggan += 1    #diubah jadi += agar tiap input menambahkan pelanggan            

    barang_saat_ini = 1
    while barang_saat_ini < jumlah_barang:  # diubah menjadi <
        print("Barang", barang_saat_ini)
        berat = int(input("Masukkan berat paket (kg): "))
        kategori = int(input("Pilih kategori (1. Standar / 2. Ekspres): "))

        harga = berat * 5000 # dari ** menjadi * karena ** merupakan perpangkatan           

        if kategori == 2:   # mengubah "=" menjadi "=="            
            biaya = 20000
            asuransi = input("Tambahkan asuransi? (y/n): ")
            if asuransi == "y":
                biaya = biaya + 15000
            elif asuransi == "n":  # menambahkan kondisi asuransi == "n" agar ketika user minginput "n" tidak error 
                biaya = 0                     
        else:
            jarak = int(input("Masukkan jarak (km): ")) #menambahkan int karena jarak merupakan bilangan bulat  
            if jarak > 100:
                biaya = 15000
            if jarak > 20:              
                biaya = 10000
            else:
                biaya = 5000

        total_barang = harga % biaya      
        total_pelanggan = total_pelanggan + total_barang
        barang_saat_ini = barang_saat_ini + 1 # dari * diubah menjadi + agar tidak stuck di 1 * 1 = 1  

    print("Total harga untuk pelanggan ini: Rp", total_pelanggan)
    total_pendapatan = total_pendapatan + total_pelanggan

    ulangi = input("Layani pelanggan lain? (y/n): ") #menghapus int karena y dan n bukan merupakan integer, melainkan string
    if ulangi == "n":
        break                             
print("Total Pendapatan Hari Ini: Rp", total_pendapatan) 

hitung = True
total_pendapatan = 0

print("Selamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang = int(input("Berapa banyak barang yang akan dikirim? "))
    total_pelanggan = 0                                   # bug 9, sharusnya mulai dr 0

    barang_saat_ini = 1
    while barang_saat_ini <= jumlah_barang:               # bug 2, seharusnya memakai "<="
        print("Barang", barang_saat_ini)
        berat = int(input("Masukkan berat paket (kg): "))
        kategori = int(input("Pilih kategori (1. Standar / 2. Ekspres): "))

        harga = berat * 5000                              # bug 4, jika ingim mengali cukup memberika "*" 1 saja karn ajika ada 2 itu perpangkatan

        if kategori == 2:                                 # bug 1, seharusnya "=" ada 2 karna membandingkan
            biaya = 20000
            asuransi = input("Tambahkan asuransi? (y/n): ")
            if asuransi == "y":
                biaya = biaya + 15000
                                                          # bug 5: biaya = 0 dihapus
        else:
            jarak = int(input("Masukkan jarak (km): "))   # bug 6, perlu menambahkan int() karna tanpa itu program akan mengira inpuan berupa string
            if jarak > 100:
                biaya = 15000
            elif jarak > 20:                              
                biaya = 10000
            else:
                biaya = 5000

        total_barang = harga + biaya                      # bug 8, bukan memakai % karna itu modulus. sementara protgam ingin variabel total ini berisi hasil jumlah hatga + biaya
        total_pelanggan = total_pelanggan + total_barang
        barang_saat_ini = barang_saat_ini + 1             # bug 3, seharusnya di tambah 1 bukan di kali 1 karna jika di kali hasil tidak akan pernah berubah

    print("Total harga untuk pelanggan ini: Rp", total_pelanggan)
    total_pendapatan = total_pendapatan + total_pelanggan

    ulangi = input("Layani pelanggan lain? (y/n): ")      # bug 10, tidak perlu memakai int() karna isi inputan berupa huruf y/n
    if ulangi == "n":
        hitung = False                                    # bug 11

print("Total Pendapatan Hari Ini: Rp", total_pendapatan)  # bug 12, saya ubah menjadi total pendapatan karna itu nama variabelnya, sementara total revenue tidak ada variabel itu 
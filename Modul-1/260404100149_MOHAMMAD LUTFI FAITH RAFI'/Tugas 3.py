jarak_sekali_jalan = 100
konsumsi_bahan_bakar = 40
sisa_bensin = 1.5
harga_bahan_bakar = 10000

total_jarak = jarak_sekali_jalan * 2 
kebutuhan_bahan_bakar = total_jarak / konsumsi_bahan_bakar
jumlah_bahan_bakar = kebutuhan_bahan_bakar - sisa_bensin
total_biaya = jumlah_bahan_bakar * harga_bahan_bakar
print("total jarak =",total_jarak)
print("kebutuhan bahan bakar =",int(kebutuhan_bahan_bakar))
print("jumlah bahan bakar =",jumlah_bahan_bakar)
print("total biaya =",total_biaya)
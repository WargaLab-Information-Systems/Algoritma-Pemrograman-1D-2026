jarak_sekali_jalan=100
konsumsi_motor=40
sisa_bensin=1.5
harga_bensin=10000

jarak_pp = jarak_sekali_jalan * 2
total_kebutuhan_bensin = jarak_pp/konsumsi_motor
bensin_beli = total_kebutuhan_bensin - sisa_bensin
biaya_bensin = bensin_beli*harga_bensin

print ("total jarak perjalanan pulang-pergi yang dibutuhkan:", jarak_pp)
print("total kebutuhan bensin yang diperlukan:", total_kebutuhan_bensin)
print("jumlah bensin yang harus dibeli:", bensin_beli)
print("total biaya bensin", biaya_bensin)
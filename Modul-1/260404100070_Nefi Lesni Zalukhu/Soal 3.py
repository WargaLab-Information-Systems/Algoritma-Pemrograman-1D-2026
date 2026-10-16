jarak_pergi = 100
jarak_pulang = 100
konsumsi = 40
bensin_awal = 1.5
harga_bensin = 10000

total_jarak = jarak_pergi + jarak_pulang

total_bensin = total_jarak / konsumsi
bensin_dibeli = total_bensin - bensin_awal
total_biaya = bensin_dibeli * harga_bensin

print("Total jarak perjalanan :", total_jarak, "km")
print("Total kebutuhan bensin :", total_bensin, "liter")
print("Bensin yang harus dibeli :", bensin_dibeli, "liter")
print("Total biaya bensin : Rp", total_biaya)
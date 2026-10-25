jarak_pergi = 100
jarak_pulang = 100
bensin = 40
sisa_bensin = 1.5
harga = 10000

total_jarak = jarak_pergi + jarak_pulang
kebutuhan_bensin = total_jarak / bensin
bensin_beli = kebutuhan_bensin - sisa_bensin
biaya = bensin_beli * harga

print("Total jarak =", total_jarak, "km")
print("Kebutuhan bensin =", kebutuhan_bensin, "liter")
print("Bensin yang dibeli =", bensin_beli, "liter")
print("Biaya bensin =", biaya)
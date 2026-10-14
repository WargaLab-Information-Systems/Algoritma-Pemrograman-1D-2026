
jarak_pergi = 100
konsumsi = 40
sisa_bensin = 1.5
harga_bensin = 10000

total_jarak = jarak_pergi * 2
total_bensin = total_jarak / konsumsi
bensin_dibeli = total_bensin - sisa_bensin
total_biaya = bensin_dibeli * harga_bensin

print ("total jarak perjalanan =", total_jarak, "km")
print ("total kebutuhan bensin =", total_bensin, "liter")
print ("bensin yang harus dibeli =", bensin_dibeli, "liter")
print ("total biaya bensin = rp", total_biaya) 

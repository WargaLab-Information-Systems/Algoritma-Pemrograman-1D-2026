jarak_pergi = 100 #Perjalanan pulang pergi km
konsumsi_bensin = 40 #Konsumsi per 1 liter
sisa_bensin = 1.5 #Sisa bensin dalam liter
harga_bensin = 10000 #Harga bensin per liter

total_jarak = jarak_pergi * 2
total_bensin = total_jarak / konsumsi_bensin
bensin_dibeli = total_bensin - sisa_bensin
total_biaya = bensin_dibeli * harga_bensin

print("total jarak perjalanan: ", total_jarak, "km")
print("total kebutuhan bensin: ", total_bensin, "liter")
print("bensin yang dibeli: ", bensin_dibeli, "liter")
print("total biaya bensin: Rp", total_biaya)
jarak= 100
konsumsi = 40       
sisa_bensin = 1.5             
harga_per_liter = 10000        

total_jarak = jarak * 2
kebutuhan_bensin = total_jarak / konsumsi
bensin_dibeli = kebutuhan_bensin - sisa_bensin
total_biaya = bensin_dibeli * harga_per_liter

print("=== Perhitungan Perjalanan Dimas ===")
print("Jarak satu arah        :", jarak, "km")
print("Total jarak pulang-pergi:", total_jarak, "km")
print("Kebutuhan bensin       :", kebutuhan_bensin, "liter")
print("Sisa bensin            :", sisa_bensin, "liter")
print("Bensin yang dibeli     :", bensin_dibeli, "liter")
print("Harga per liter        : Rp", harga_per_liter)
print("Total biaya            : Rp", int(total_biaya))
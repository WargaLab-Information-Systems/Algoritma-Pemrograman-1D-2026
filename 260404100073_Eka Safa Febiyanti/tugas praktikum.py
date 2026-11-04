

# ==== Perjalanan dimas dan bahan bakar ====

jarak = 100
konsumsi = 40
sisa_bensin = 1.5
harga_bensin = 10000

total_jarak = jarak * 2
kebutuhan_bensin = total_jarak / konsumsi
bensin_dibeli = kebutuhan_bensin - sisa_bensin
total_biaya = bensin_dibeli * harga_bensin

print("Total jarak =", total_jarak, "km")
print("kebutuhan bensin =", bensin_dibeli, "liter")
print("bensin yang dibeli =", bensin_dibeli, "liter")
print("total biaya = Rp", total_biaya)
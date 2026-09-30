jarak = 100
konsumsi = 40
sisa_bensin = 1.5
harga_bensin = 10000

jarak_perjalanan = jarak * 2
kebutuhan_bensin = jarak_perjalanan / konsumsi
bensin_dibeli = kebutuhan_bensin - sisa_bensin
biaya = bensin_dibeli * harga_bensin

print("Total jarak perjalanan :", jarak_perjalanan, "km")
print("Kebutuhan bensin      :", kebutuhan_bensin, "liter")
print("Bensin yang dibeli       :", bensin_dibeli, "liter")
print("Total biaya            : Rp", round(biaya))
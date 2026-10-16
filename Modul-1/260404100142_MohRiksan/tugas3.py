jarak = 100
konsumsi = 40
sisa_bensin = 1.5
harga = 10000

total_jarak = jarak * 2
kebutuhan = total_jarak / konsumsi
beli = kebutuhan - sisa_bensin
biaya = beli * harga

print("Total jarak pulang-pergi =", total_jarak, "km")
print("Total kebutuhan bensin =", kebutuhan, "liter")
print("Bensin yang harus dibeli =", beli, "liter")
print("Total biaya = Rp", int(biaya))
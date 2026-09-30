jarak_sekali_jalan=100
konsumsi=40
sisa_bensin=1.5
harga_bensin=10000

total_jarak=jarak_sekali_jalan*2
total_bensin=total_jarak / konsumsi
beli_bensin=total_bensin-sisa_bensin
total_biaya=beli_bensin * harga_bensin

print("Total jarak pulang-pergi:", total_jarak, "km")
print("Total kebutuhan bensin:", total_bensin, "liter")
print("Bensin yang harus dibeli:", beli_bensin, "liter")
print("Total biaya: Rp", total_biaya)

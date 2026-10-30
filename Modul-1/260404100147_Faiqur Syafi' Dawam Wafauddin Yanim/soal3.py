jarak = 100
konsumsi_bbm = 40
sisa_bbm = 1.5
harga_bbm = 10000

total_jarak = jarak * 2
total_bensin = total_jarak / konsumsi_bbm
bensin_dibeli = total_bensin - sisa_bbm
total_biaya = bensin_dibeli * harga_bbm

print("Total jarak yang ditempuh: ",total_jarak,"km")
print("Kebutuhan bensin untuk seluruh perjalanan: ",total_bensin,"liter")
print("Bensin yang benar-benar harus dibeli: ",bensin_dibeli,"liter")
print("Total biaya yang harus dikeluarkan: Rp.",total_biaya)
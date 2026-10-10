Jarak_Pergi = float(input("masukkan jarak pergi (km): "))
Jarak_Pulang = float(input("masukkan jarak pulang (km); "))
konsumsi = float(input("masukkan konsumsi motor (km/liter); "))
bensin_tersedia = float(input("Bensin yang tersedia (liter): "))
harga_bensin = float(input("masukkan harga bensin per liter: "))

total_jarak = Jarak_Pergi + Jarak_Pulang
kebutuhan_bensin = total_jarak / konsumsi
bensin_dibeli = kebutuhan_bensin - bensin_tersedia
total_biaya = bensin_dibeli * harga_bensin

print("Total Jarak =", total_jarak, "km")
print("Kebutuhan Bensin =", kebutuhan_bensin, "liter")
print("Bensin yang harus dibeli =", bensin_dibeli, "liter")
print("Total biaya = Rp", total_biaya)

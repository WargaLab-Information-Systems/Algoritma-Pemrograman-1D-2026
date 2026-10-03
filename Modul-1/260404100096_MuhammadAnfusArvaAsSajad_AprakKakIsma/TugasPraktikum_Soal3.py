jarak_sekali_jalan = 100      # km
konsumsi = 40                 # km per liter
sisa_bensin = 1.5             # liter
harga_per_liter = 10000       # Rp per liter

# ===== PROSES PERHITUNGAN =====
total_jarak = jarak_sekali_jalan * 2
total_kebutuhan_bensin = total_jarak / konsumsi
liter_bensin_yang_dibeli = total_kebutuhan_bensin - sisa_bensin
total_biaya = liter_bensin_yang_dibeli * harga_per_liter

# ===== OUTPUT =====
print("Total jarak pulang-pergi      :", total_jarak, "km")
print("Total kebutuhan bahan bakar   :", total_kebutuhan_bensin, "liter")
print("Bahan bakar yang harus dibeli :", liter_bensin_yang_dibeli, "liter")
print("Total biaya                   : Rp", total_biaya)
print("=== PROGRAM PERENCANAAN PERJALANAN DIMAS ===")

jarak_satu_arah = 100  # km
konsumsi_bbm_per_liter = 40  # 40 km untuk setiap 1 liter
bensin_di_tangki = 1.5  # liter
harga_bbm_per_liter = 10000  # Rp10.000 per liter

total_jarak = jarak_satu_arah * 2

total_kebutuhan_bbm = total_jarak / konsumsi_bbm_per_liter

bbm_yang_harus_dibeli = total_kebutuhan_bbm - bensin_di_tangki

total_biaya = bbm_yang_harus_dibeli * harga_bbm_per_liter

print("-" * 50)
print(f"Total Jarak Pulang-Pergi          : {total_jarak} km")
print(f"Total Kebutuhan Bahan Bakar       : {total_kebutuhan_bbm} liter")
print(f"Bahan Bakar yang Harus Dibeli     : {bbm_yang_harus_dibeli} liter")
print(f"Total Biaya yang Harus Dikeluarkan: Rp {total_biaya:,.0f}")
print("-" * 50)
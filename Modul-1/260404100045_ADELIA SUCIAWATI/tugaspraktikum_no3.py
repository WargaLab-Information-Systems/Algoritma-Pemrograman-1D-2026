#Diketahui
jarak_tempuh_awal = 100 #km
konsumsi_bbm = 40 #km perliter
sisa_indikator_bensin = 1.5 #liter
harga_bensin = 10000 #perliter

jarak_pp = jarak_tempuh_awal * 2
kebutuhan_bbm = jarak_pp / konsumsi_bbm
bbm_yang_harusdibeli = kebutuhan_bbm - sisa_indikator_bensin
total_biaya_keluar = bbm_yang_harusdibeli * harga_bensin

print("Total jaraK PP", jarak_pp)
print("Total BBM seluruh perjalanan", kebutuhan_bbm)
print("Total BBM yang harus dibeli", bbm_yang_harusdibeli)
print("Total Biaya yang harus keluar", total_biaya_keluar)
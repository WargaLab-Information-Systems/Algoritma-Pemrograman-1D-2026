jarak_satu_arah = 100
konsumsi_bensin = 40
sisa_bbm = 1.5
harga_bbm_per_liter = 10000

total_jarak_pp = jarak_satu_arah*2
total_kebutuhan_bbm = total_jarak_pp / konsumsi_bensin
bbm_harus_beli = total_kebutuhan_bbm - sisa_bbm
total_biaya = bbm_harus_beli*harga_bbm_per_liter

print("total jarak pp:", total_jarak_pp)
print("total kebutuhan bbm", total_kebutuhan_bbm)
print("bbm harus beli", bbm_harus_beli)
print("total biaya", total_biaya)

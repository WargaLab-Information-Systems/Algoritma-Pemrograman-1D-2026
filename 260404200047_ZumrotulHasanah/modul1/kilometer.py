jarak_tujuan = 100
konsumsi_Bbm = 40
sisa_bensin = 1.5
harga_bensin = 10000


total_jarak = jarak_tujuan * 2
kebutuhanBbm = total_jarak / konsumsi_Bbm
beli_Bbm = kebutuhanBbm - sisa_bensin
total_biaya = beli_Bbm * harga_bensin

print("total jarak pulang-pergi : ", total_jarak)
print("kebutuhan bahan bakar : ", total_jarak)
print("jumlah bahan bakar yang dibeli : ", beli_Bbm)
print("total biaya keluar : Rp.", total_biaya)
print("=== JARAK DIMAS KE RUMAH KELUARGA ===")
jarak = 100 
konsumsi_bahan_bakar = 40
sisa_bahan_bakar_dimas = 1.5
harga_bahan_bakar = 10000

total_jarak_perjalanan = jarak * 2
total_kebutuhan_bahan_bakar = total_jarak_perjalanan /  konsumsi_bahan_bakar
jumlah_bahan_bakar_dibeli = total_kebutuhan_bahan_bakar - sisa_bahan_bakar_dimas
total_biaya = int(jumlah_bahan_bakar_dibeli * harga_bahan_bakar)


print("total jarak pulang pergi =", total_jarak_perjalanan, )
print("total kebutuhan bahan bakar =", total_kebutuhan_bahan_bakar , )
print("total bahan bakar dibeli =", jumlah_bahan_bakar_dibeli,)
print("total biaya yang di keluarkan =", total_biaya)
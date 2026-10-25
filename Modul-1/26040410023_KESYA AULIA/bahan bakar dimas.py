jarak = 100
kemampuan_motor = 40 
sisa = 1.5
harga = 10000

total_jarak = 100 * 2
print("total jarak perjalanan pulang pergi: ", total_jarak, "km")

jumlah_bbm = total_jarak / kemampuan_motor
print("total bahan bakar seluruh perjalanan: ",jumlah_bbm, "liter")

yang_dibutuhkan = jumlah_bbm - sisa
print("jumlah bahan bakar yang harus di beli: ", yang_dibutuhkan, "liter")

biaya = harga * yang_dibutuhkan
print("total biaya yang harus di keluarkan: ", biaya)
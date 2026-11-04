jarak = 100
konsumsiBbm = 40
sisaBbm = 1.5
hargaBbm = 10000
# nama = "zay"

jarakPp = jarak * 2
kebutuhanBbm = jarakPp / konsumsiBbm
beliBbm = kebutuhanBbm - sisaBbm

total = beliBbm * hargaBbm

# print(f"Jarak PP              : {jarakPp} km")
# print(f"Kebutuhan BBM         : {kebutuhanBbm} liter")
# print(f"BBM yang harus dibeli : {beliBbm} liter")
# print(f"Total biaya BBM       : Rp{int(total)}")
# print(f"Nama saya adalah {nama}")


print("Jarak PP : ", jarakPp, "km.") 
print("Kebutuhan BBM : ", kebutuhanBbm, "liter.")
print("BBM yang harus dibeli : ", beliBbm, "liter.")
print("Total biaya BBM : ", "Rp",int(total))

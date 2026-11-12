jari_jari = float(input("Masukkan jari-jari alas (cm) : "))
tinggi = float(input("Masukkan tinggi kerucut (cm) : "))

volume = round(3.14 * jari_jari ** 2 * tinggi / 3, 2)
volume2 = (1/3 * 3.14 * jari_jari ** 2 * tinggi)
print("Volume kerucut :", volume, "cm3")
print(volume2)
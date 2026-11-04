# ==== menghitung volume kerucut ====
import math 

r = float(input("Masukkan jari-jari :"))
t = float(input("Masukkan tinggi: "))

Volume = (1/3) * math.pi * r * r * t

print("volume kerucut =", Volume, "cm3")
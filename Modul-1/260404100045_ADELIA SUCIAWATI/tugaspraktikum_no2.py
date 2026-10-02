r = float(input("Masukkan r alas (cm): "))
t = float(input("Masukkan t kerucut (cm): "))

# karena jari-jari alas kerucut tersebut 7 maka nilai pi yang di pakai pi=22/7
pi = 22/7
# rumus v kerucut
v = (1/3) * pi * (r ** 2) * t

print("Hasil volume kerucut=", v, "cm3")
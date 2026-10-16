# Program Pemantau Reaktor Krasny

suhu = float(input("Masukkan suhu reaktor (Celsius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

# Menentukan pesan status bahaya
if suhu > 1000:
    if tekanan > 50:
        pesan = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        pesan = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
 
 pesan = "tekanan tidak stabil" if tekanan > 30 else "tekanan stabil"

else:
    pesan = "Reaktor Belum Cukup Panas"

# Ternary operator untuk status pompa
pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

# Tampilkan hasil
print("Suhu              :", int(suhu), "derajat Celsius")
print("Tekanan           :", int(tekanan), "Bar")
print("Status reaktor    :", pesan)
print("Status pompa      :", pompa)
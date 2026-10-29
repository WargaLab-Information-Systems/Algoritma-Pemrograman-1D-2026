suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

print("Suhu reaktor:", suhu, "°C")
print("Tekanan gas:", tekanan, "Bar")

if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI! REAKOR NAK MELETUP!"
    else:
        status = "Bahaya Suhu: Segera Turunkan Daya!"

elif suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"


else:
    status = "Reaktor Belum Cukup Panas"

print("Status bahaya reaktor:", status)

pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("Status pompa:", pompa)
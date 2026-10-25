suhu = int(input("Masukkan suhu reaktor: "))
tekanan = int(input("Masukkan tekanan gas: "))
if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"
else:
    status = "Reaktor Belum Cukup Panas"

print("Suhu     :", suhu, "derajat")
print("Tekanan  :", tekanan, "Bar")
print("Status   :", status)

pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print("Pompa    :", pompa)
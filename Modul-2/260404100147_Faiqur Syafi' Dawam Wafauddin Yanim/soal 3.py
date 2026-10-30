suhu = float(input("Masukkan suhu reaktor (Celcius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))


if suhu > 1000:
    if tekanan > 50:
        pesan = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        pesan = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500: 
    if tekanan > 30:
        pesan = "Tekanan Tidak Stabil"
    else:
        pesan = "Operasi Reaktor Normal"
else:
    pesan = "Reaktor Belum Cukup Panas"


status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"


print("Suhu:", suhu , "C tekanan : ", tekanan," Bar")
print("Status:", pesan)
print("Pompa:", status_pompa)
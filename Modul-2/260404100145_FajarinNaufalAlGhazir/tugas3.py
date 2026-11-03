suhu = int(input("Suhu reaktor (dalam Celcius): "))
tekanan = int(input("Tekanan gas (dalam bar): "))

if suhu > 1000:
    if tekanan > 50:
        peringatan = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        peringatan = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        peringatan = "Tekanan Tidak Stabil"
    else:
        peringatan = "Operasi Reaktor Normal"
else:
    peringatan = "Reaktor Belum Cukup Panas"
    
print(f"Suhu                    : {suhu}c")
print(f"Tekanan                 : {tekanan} Bar")
print(f"Pesan Status Reaktor    : {peringatan}")
print("Pompa Maksimal") if suhu > 800 else print("Pompa Normal")
suhu = int(input("Masukkan suhu reaktor (celcius): "))
tekanan = int(input("masukkan tekanan gas (bar)"))

if suhu >1000:
    if tekanan > 50:
        print("MELTDOWN! SEGERA EVAKUASI!")
    else:
        print("Bahaya suhu: segera turunkan daya!")
elif suhu > 500:
    if tekanan > 30:
        print("tekanan tidak stabil")
    elif tekanan < 30:
        print("operasi reaktor normal")
    
else:
    print("reaktor belum cukup panas")
if suhu >800:
    print("pompa maksimal")
else:
    print("pompa normal")

# pompa = "pompa maksimal" if suhu > 800 else "pompa normal"
# print("status pompa air:", pompa)


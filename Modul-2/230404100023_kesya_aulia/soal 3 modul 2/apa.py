
suhu = int(input("berapa suhu reaktor: "))
tekanan = int(input("berapa tekanan gas: "))

if suhu > 1000 and tekanan > 50:
    print(" MELTDOWN! SEGERA EVAKUASI!")
elif suhu > 1000 and tekanan <= 50:
    print("bahaya suhu: segera turunkan daya!")
elif suhu > 500 and tekanan > 30:
    print(" tekanan tidak stabil")
elif suhu > 500 or tekanan <= 30:
    print("operasi reaktor normal")
else:
    print("reaktor belom cukup panas")

status_pompa = "pompa maksimal" if suhu >= 800 else "pompa normal"
print("status operasional pompa air: ", status_pompa)
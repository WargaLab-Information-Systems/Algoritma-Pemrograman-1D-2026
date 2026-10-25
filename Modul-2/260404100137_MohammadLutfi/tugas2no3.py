suhu=int(input("masukkan suhu:" ))
gas= int(input("masukkan tekanan gas:" ))

if suhu > 1000:
    print("mengecek gas")
    gash = "meldown segera evakuasi" if gas> 50 else "bahaya turunkan daya"
    print(gash)
elif suhu > 500:
    print("mengecek tekanan gas")
    if gas >30:
        print("Operasi Reaktor stabil")
    else:
        print("Operasi Reaktor Normal")
else:
    print("reaktor belum cukup panas")
pompa= "pompa maksimal" if suhu > 800 else " pompa normal"
print(pompa)

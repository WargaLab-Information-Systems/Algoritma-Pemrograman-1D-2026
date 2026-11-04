suhu = int(input("Masukkan Suhu Reaktor: "))
tekananGas = int(input("Masukkan Tekanan Gas: "))

if suhu >1000 :
    if tekananGas > 50 :
        peringatan = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        peringatan = "Bahaya Suhu: Segera Turunkan Daya!"
if suhu > 500 :
    if tekananGas > 30 :
        peringatan = "Tekanan Tidak Stabil!"
    else:
        peringatan = "Operasi Reaktor Normal!"
else:
    peringatan = "Reaktor Belum Cukup Panas!"

print("Suhu                  : ", suhu)
print("Tekanan Gas           : ", tekananGas)
print("Peringatan Reaktor    : ", peringatan)
print("Pompa Maksimal!") if suhu >= 800 else print("Pompa Normal!")
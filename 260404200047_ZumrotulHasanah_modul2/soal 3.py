# Input suhu dan tekanan
suhu = int(input("Masukkan Suhu: "))
tekanan = int(input("Masukkan Tekanan:"))


# Menentukan status bahaya reaktor
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

# Menampilkan input
print("Suhu reaktor :", suhu, "°C")
print("Tekanan gas  :", tekanan, "Bar")

# Menampilkan status bahaya
print("Status Reaktor :", status)

# Ternary operator untuk pompa
pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("Status Pompa :", pompa)
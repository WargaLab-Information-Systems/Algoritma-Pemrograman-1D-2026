# 1. Input Suhu dan Tekanan
suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

# 2. Pengecekan Kondisi Bersarang (Nested IF)
if suhu > 1000:
    if tekanan > 50:
        pesan_status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        pesan_status = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        pesan_status = "Tekanan Tidak Stabil"
    else:
        pesan_status = "Operasi Reaktor Normal"
else:
    pesan_status = "Reaktor Belum Cukup Panas"

# 3. Status Pompa Air Menggunakan Ternary Operator
status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

# 4. Output Hasil Pemrosesan
print("=== LAPAN SISTEM PEMANTAUAN REAKTOR ===")
print(f"Suhu Reaktor   : {suhu} °C")
print(f"Tekanan Gas    : {tekanan} Bar")
print(f"Status Bahaya  : {pesan_status}")
print(f"Status Pompa   : {status_pompa}")
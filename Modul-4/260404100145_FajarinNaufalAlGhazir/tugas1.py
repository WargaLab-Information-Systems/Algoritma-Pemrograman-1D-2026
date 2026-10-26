barisLampu = int(input("Masukkan jumlah baris lampu: "))
lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))
print("-" * 50)

lampuke = 1
for baris in range(1, barisLampu + 1):
    print(f"Baris ke-{baris}")
    for lamp in range(1, lampu + 1):
        if lamp % 3 == 0:
            print(f"Lampu ke-{lampuke} mengalami gangguan.")
        else:
            print(f"Lampu ke-{lampuke} berfungsi normal.")
        lampuke += 1
    print("-" * 30) 
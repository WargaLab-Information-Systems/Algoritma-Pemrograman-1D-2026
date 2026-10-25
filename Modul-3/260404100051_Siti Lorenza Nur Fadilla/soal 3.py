jumlah = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
total = 0
tertinggi = -1
terendah = 101
 
for i in range(10):
    nama = input("Nama: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
 
    akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4
 
    if akhir >= 85:
        kategori = "A"
    elif akhir >= 75:
        kategori = "B"
    elif akhir >= 65:
        kategori = "C"
    elif akhir >= 50:
        kategori = "D"
    else:
        kategori = "E"
 
    jumlah[kategori] += 1
    total += akhir
    print(nama, tugas, uts, uas, "| Akhir:", round(akhir, 2), "| Kategori:", kategori)
 
    if akhir > tertinggi:
        tertinggi = akhir
        nama_tinggi = nama
    if akhir < terendah:
        terendah = akhir
        nama_rendah = nama
 
print("Jumlah per kategori:", jumlah)
print("Tertinggi:", round(tertinggi, 2), "-", nama_tinggi)
print("Terendah :", round(terendah, 2), "-", nama_rendah)
print("Rata-rata:", round(total / 10, 2))
 
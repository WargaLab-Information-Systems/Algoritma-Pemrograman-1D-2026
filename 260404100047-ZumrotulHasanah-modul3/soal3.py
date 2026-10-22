mahasiswa = []

for i in range(10):
    print("\nMahasiswa ke-", i + 1)

    nama = input("Nama mahasiswa: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    akhir = tugas * 0.30 + uts * 0.30 + uas * 0.40

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

    data = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir,
        "kategori": kategori
    }

    mahasiswa.append(data)

print("\n=== DAFTAR NILAI MAHASISWA ===")

for m in mahasiswa:
    print("\nNama:", m["nama"])
    print("Nilai tugas:", m["tugas"])
    print("Nilai UTS:", m["uts"])
    print("Nilai UAS:", m["uas"])
    print("Nilai akhir:", round(m["akhir"], 2))
    print("Kategori:", m["kategori"])

print("\n=== REKAPITULASI KATEGORI ===")

for kategori in ["A", "B", "C", "D", "E"]:
    jumlah = 0

    for m in mahasiswa:
        if m["kategori"] == kategori:
            jumlah += 1

    print("Kategori", kategori, ":", jumlah, "mahasiswa")

tertinggi = max(mahasiswa, key=lambda m: m["akhir"])
terendah = min(mahasiswa, key=lambda m: m["akhir"])

rata_rata = sum(m["akhir"] for m in mahasiswa) / len(mahasiswa)

print("\n=== RINGKASAN KELAS ===")
print("Nilai tertinggi:", tertinggi["nama"],
      "-", round(tertinggi["akhir"], 2))
print("Nilai terendah:", terendah["nama"],
      "-", round(terendah["akhir"], 2))
print("Rata-rata kelas:", round(rata_rata, 2))
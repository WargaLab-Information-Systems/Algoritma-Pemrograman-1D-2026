asisten = []
while True:
    nama = input("Masukkan nama asisten (ketik 'cukup' untuk berhenti): ")
    if nama.lower() == "cukup":
        break
    asisten.append(nama)
    
asistenAwal = tuple(asisten)
    
asistenTambahan = input("Masukkan nama asisten tambahan : ")
asistenAkhir = asistenAwal + (asistenTambahan,)

hari = []
while True:
    namaHari = input("Masukkan nama hari: ")
    if namaHari.lower() == "cukup":
        break
    hari.append(namaHari)
    
hariAkhir = tuple(hari)

namaIzin = input("Masukkan nama asisten yang dikecualikan : ")
hariIzin = input("Masukkan nama hari pengecualiannya : ")

for nama in asistenAkhir:
    for namaHari in hariAkhir:
        if nama.lower() == namaIzin.lower() and namaHari.lower() == hariIzin.lower():
            continue
        print(nama, "-", namaHari)
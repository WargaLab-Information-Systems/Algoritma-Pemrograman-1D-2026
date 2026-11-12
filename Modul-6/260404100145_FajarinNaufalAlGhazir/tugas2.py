dataAsisten = ()
dataHari = ()

while True:
    inputData = input("Masukkan nama-nama asisten ('cukup' untuk selesai): ")
    if inputData == "cukup":
        break
    else:
        dataAsisten += (inputData,)

asistenDadakan = input("Masukkan nama asisten dadakan: ")
dataAsisten += (asistenDadakan,)

while True:
    inputHari = input("Masukkan nama hari tugas ('cukup' untuk selesai): ")
    if inputHari == "cukup":
        break
    else:
        dataHari += (inputHari,)
print("-" * 30)

dataAsistenLs = list(dataAsisten)
dataHariLs = list(dataHari)
print(dataAsistenLs)
print(dataHariLs)
print("-" * 30)

asistenKecuali = input("Masukkan nama asisten pengecualian: ")
hariKecuali = input("Masukkan nama hari pengecualian: ")
print("-" * 30)

for i in dataAsistenLs:
    print(f"Nama asisten: {i}")
    for j in dataHariLs:
        if i == asistenKecuali and j == hariKecuali:
            continue
        print(f"- {j}")
    print("-" * 30)
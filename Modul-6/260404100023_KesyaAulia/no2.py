nama_asisten = []
hari_kerja = []
while True:
    nama = input("masukkan nama asisten :")
    if nama == "cukup":
        break
    nama_asisten.append(nama)

asisten_fiks = tuple(nama_asisten)
print (type(asisten_fiks))

nama_tambahan = input("masukkan nama asisten tambahan :")
asisten_fiks += (nama_tambahan,)

while True:
    hari = input("masukkan hari kerja asisten :")
    if hari == "cukup":
        break
    hari_kerja.append(hari)

kecuali_nama = input("masukkan nama asisten yang tidak kerja :")
kecuali_hari = input("masukkan hari kerja asisten yang tidak kerja :")
while kecuali_nama not in asisten_fiks:
    print("nama tidak valid")
    kecuali_nama = input("masukkan nama asisten yang tidak kerja :")

for i in asisten_fiks:    
    for j in hari_kerja:
        if i == kecuali_nama and j == kecuali_hari:
            continue
total_nilai = 0
kategori_A = 0
kategori_B = 0
kategori_C = 0
kategori_D = 0
kategori_E = 0

for i in range (1, 11):
    nama = input("masukkan nama mahasiswa: ")
    tugas = int(input("masukkan nilai tugas: "))
    uts = int(input("masukkan nilai uts: "))
    uas = int(input("masukkan nilai uas: "))

    nilai_akhir = (tugas * 30/100) + (uts * 30/100) + (uas * 40/100)
    print("nilai akhir mahasiswa: ", nilai_akhir)

    total_nilai += nilai_akhir

    if i == 1:
        nilai_tertinggi = nilai_akhir
        nilai_terendah = nilai_akhir
        nama_tertinggi = nama
        nama_terendah = nama
    else:
        if nilai_akhir > nilai_tertinggi:
            nilai_tertinggi = nilai_akhir
            nama_tertinggi = nama

        if nilai_akhir < nilai_terendah:
            nilai_terendah = nilai_akhir
            nama_terendah = nama    
    

    if nilai_akhir >=85:
        print("mendapat A")
        kategori_A +=1
    elif nilai_akhir >=75:
        print("mendapat B")
        kategori_B +=1
    elif nilai_akhir >=65:
        print("mendapat C")
        kategori_C +=1
    elif nilai_akhir >=50:
        print("mendapat D")
        kategori_D +=1
    else:
        print("mendapat E")
        kategori_E +=1

    print("banyak mahasiswa medapat kategori A: ", kategori_A)
    print("banyak mahasiswa medapat kategori B: ", kategori_B)
    print("banyak mahasiswa medapat kategori C: ", kategori_C)
    print("banyak mahasiswa medapat kategori D: ", kategori_D)
    print("banyak mahasiswa medapat kategori E: ", kategori_E)

    print("nilai tertinggi: ", nilai_tertinggi, "oleh mahasiswa: ", nama_tertinggi) 
    print("nilai terendah: ", nilai_terendah, "oleh mahasiswa: ", nama_terendah)

    rata_rata = total_nilai / 10    
    print("rata-rata nilai akhir: ", rata_rata)
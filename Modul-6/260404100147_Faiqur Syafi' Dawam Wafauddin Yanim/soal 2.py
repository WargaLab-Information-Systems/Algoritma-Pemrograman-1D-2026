def penjadwalan_lab():
    print("\nSistem Penjadwalan Shift Asisten Laboratorium")
    asisten_awal = []
    print("Masukkan nama-nama asisten awal (ketik 'cukup' untuk berhenti):")
    while True:
        nama = input("Asisten: ")
        if nama == "cukup":
            break
        if nama:
            asisten_awal.append(nama)
            
    
    tuple_asisten_awal = tuple(asisten_awal)

    nama_tambahan = input("Masukkan satu nama asisten tambahan yang mendadak bergabung: ")
    
    asisten_akhir = tuple_asisten_awal + (nama_tambahan,)
    
    hari_tugas = []
    print("\nMasukkan nama-nama hari tugas (ketik 'cukup' untuk berhenti):")
    while True:
        h = input("Hari: ")
        if h == "cukup":
            break
        if h:
            hari_tugas.append(h)
    tuple_hari = tuple(hari_tugas)
    
    print("\nInput Pengecualian Jadwal")
    asisten_pengecualian = input("Masukkan nama asisten untuk pengecualian: ")
    hari_pengecualian = input("Masukkan hari spesifik untuk pengecualian: ")
    
    print("\nJadwal Shift Asisten Laboratorium")
    for asisten in asisten_akhir:
        for hari in tuple_hari:
            if asisten == asisten_pengecualian and hari == hari_pengecualian:
                continue
            print(f"Asisten: {asisten} | Hari: {hari}")

penjadwalan_lab()
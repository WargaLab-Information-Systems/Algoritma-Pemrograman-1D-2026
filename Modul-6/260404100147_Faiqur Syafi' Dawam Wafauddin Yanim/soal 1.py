def pendaftaran_robotika():
    daftar_nama = []
    
    print("Pendaftaran Anggota Klub Robotika")
    print("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti):")
    
    while True:
        nama = input("Masukkan nama: ")
        if nama == "selesai":
            break
        if nama:
            daftar_nama.append(nama)
            
    print("\nEvaluasi Data Pendaftaran")
    validitas = {}
    for nama in daftar_nama:
        if nama == "admin" or len(nama) < 4:
            validitas[nama] = "Tidak Valid"
            print(f"Nama '{nama}': Tidak valid (Menggunakan nama 'admin' atau panjang < 4 karakter).")
        else:
            validitas[nama] = "Valid"
            print(f"Nama '{nama}': Valid")
            
    penyusup = input("\nMasukkan nama spesifik yang dicurigai sebagai penyusup untuk dihapus: ")
    
    if penyusup in daftar_nama:
        daftar_nama.remove(penyusup)
        print(f"Berhasil menghapus '{penyusup}' dari sistem.")
    else:
        print(f"Nama penyusup '{penyusup}' tidak ditemukan di dalam pendaftaran.")
        
    print("\nDaftar Nama Akhir:", daftar_nama)

pendaftaran_robotika()
def hitung_nilai_mahasiswa(nama, tugas, uts, uas):
    nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)
    
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"
        
    status = "Lulus" if grade in ["A", "B", "C"] else "Tidak Lulus"
    
    print("\n--- HASIL PENILAIAN AKADEMIK ---")
    print(f"Nama Mahasiswa : {nama}")
    print(f"Nilai Akhir    : {nilai_akhir:.2f}")
    print(f"Grade          : {grade}")
    print(f"Status         : {status}")


nama_mhs = input("Masukkan nama mahasiswa: ")
n_tugas = float(input("Masukkan nilai tugas: "))
n_uts = float(input("Masukkan nilai UTS: "))
n_uas = float(input("Masukkan nilai UAS: "))

hitung_nilai_mahasiswa(nama_mhs, n_tugas, n_uts, n_uas)
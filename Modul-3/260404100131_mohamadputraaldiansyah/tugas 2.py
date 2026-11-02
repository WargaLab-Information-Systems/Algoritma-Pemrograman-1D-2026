while True:
    try:
        n = int(input("Masukkan tinggi setengah menara (2-15): "))
    except ValueError:
        print("Harus berupa angka bulat!")
        continue

    if 2 <= n <= 15:
        break
    print("Nilai harus antara 2 sampai 15!")



def buat_baris(k):
    teks = ""
    for angka in range(1, k + 1):
        teks += str(angka % 10)
    for angka in range(k - 1, 0, -1):
        teks += str(angka % 10)
    return teks



lebar = 2 * n - 1


for k in range(1, n + 1):
    print(buat_baris(k).center(lebar).rstrip())


for k in range(n - 1, 0, -1):
    print(buat_baris(k).center(lebar).rstrip())
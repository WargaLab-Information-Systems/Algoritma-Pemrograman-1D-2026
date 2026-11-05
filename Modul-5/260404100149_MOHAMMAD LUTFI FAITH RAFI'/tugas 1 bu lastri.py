def hitung_pelanggan(n):
    if n == 1 or n == 2:
        return 1
    else:
        return hitung_pelanggan(n - 1) + hitung_pelanggan(n - 2) #dua hari sebelum

while True: #biar user bener" memasukkan angka positif 
 hari = int(input("Masukkan hari ke-: "))
 if hari > 0:
    hasil = hitung_pelanggan(hari)
    print("Jumlah pelanggan pada hari ke-", hari, "adalah:", hasil)
    break 
 else:
    print("Hari harus berupa bilangan positif!")
    continue

      

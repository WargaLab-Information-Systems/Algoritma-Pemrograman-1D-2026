def cek_palindrom(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
        return True
    else:
        return False

teks = input("Masukkan sebuah kata: ")

hasil = cek_palindrom(teks)

if hasil == True:
    print(teks, "adalah kata palindrom")
else:
    print(teks, "bukan kata palindrom")
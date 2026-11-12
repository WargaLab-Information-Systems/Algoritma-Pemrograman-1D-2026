def cek_palindrom(kata):
    kata = kata.lower()

    if kata == kata[::-1]: 
        return True
    else:
        return False

kata = input("Masukkan sebuah kata: ")
hasil = cek_palindrom(kata)

if hasil:
    print(kata, "termasuk kata palindrom")
else:
    print(kata, "bukan kata palindrom")
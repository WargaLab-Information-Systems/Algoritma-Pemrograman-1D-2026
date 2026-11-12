def cekPalindrom(kata):
    kata = kata.lower()
    kebalikan = ""
    for huruf in kata:
        kebalikan = huruf + kebalikan
    return kata == kebalikan


kata = input("Masukkan sebuah kata: ")
hasil = cekPalindrom(kata)

print("Nilai kembalian fungsi:", hasil)
if hasil:
    print(f"Kata '{kata}' merupakan palindrom.")
else:
    print(f"Kata '{kata}' bukan palindrom.")
def cek_palindrom(kata):
    kata_bersih = kata.replace(" ", "")
    return kata_bersih == kata_bersih[::-1]


kata_input = input("Masukkan sebuah kata: ")
hasil = cek_palindrom(kata_input)

if hasil:
    print(f"Kata '{kata_input}' adalah Palindrom (True).")
else:
    print(f"Kata '{kata_input}' bukan Palindrom (False).")
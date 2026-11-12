def cek_palindrom(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
        return True
    else:
        return False

kata = input("Masukkan kata: ")
hasil = cek_palindrom(kata)

if hasil:
    print(f"Kata '{kata}' adalah palindrom (True)")
else:
    print(f"Kata '{kata}' bukan palindrom (False)")
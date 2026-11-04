
def palindrom(kata):
    if kata == kata[::-1]:
        return True

teks = input("Masukkan sebuah kata: ")

hasil = palindrom(teks)

if hasil:
    print("Kata tersebut adalah palindrom")
else:
    print("Kata tersebut bukan palindrom")

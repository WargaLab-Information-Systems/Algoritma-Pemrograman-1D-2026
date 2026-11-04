kata = input("Masukkan sebuah kata: ")

def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False


hasil = palindrom(kata)

if hasil == True:
    print("Kata tersebut adalah palindrom")
else:
    print("Kata tersebut bukan palindrom")


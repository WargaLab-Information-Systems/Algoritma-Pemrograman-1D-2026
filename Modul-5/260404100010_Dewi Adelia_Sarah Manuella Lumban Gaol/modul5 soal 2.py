def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False
        
kata = input("Masukkan sebuah kata: ")

if palindrom(kata):
    print("Kata tersebut adalah palindrom")
else:
    print("Kata tersebut bukan palindrom")



    
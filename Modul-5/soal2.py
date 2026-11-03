def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

kata = input("Masukkan kata : ")

if palindrom(kata):
    print(kata, "adalah palindrom")
else:
    print(kata, "bukan palindrom")
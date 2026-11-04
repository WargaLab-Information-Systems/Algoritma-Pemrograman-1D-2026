kata = input("masukkan kata yang mau di cek:")
def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

if palindrom(kata):
    print(kata, "adalah palindrom")
else:
    print(kata, "bukan palindrom")

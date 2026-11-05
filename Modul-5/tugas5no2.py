def palindrom(kata):
    balik = ""
    i = len(kata) - 1

    while i >= 0:
        balik += kata[i]
        i -= 1

    return kata == balik

kata = input("Masukkan kata: ")
hasil = palindrom(kata)
print("Hasil:", hasil)

if hasil:
    print("Palindrom")
else:
    print("Bukan palindrom")
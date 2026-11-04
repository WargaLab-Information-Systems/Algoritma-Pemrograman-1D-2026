# def palindrom(kata):
#     kata = kata.lower()
#     return kata == kata[::-1]
 
# kata = input("Masukkan sebuah kata: ")
# hasil = palindrom(kata)
 
# print("Hasil fungsi:", hasil)
# if hasil:
#     print("Kata '" + kata + "' adalah palindrom")
# else:
#     print("Kata '" + kata + "' bukan palindrom")






def palindrom(kata):
    balik = ""
    for huruf in kata:
        # balik = huruf + balik
        return True if kata == balik else False

kata = str(input("Masukkan kata : ")).lower() 
print(kata, "adalah palindrom") if palindrom(kata) else print(kata, "bukan palindrom")

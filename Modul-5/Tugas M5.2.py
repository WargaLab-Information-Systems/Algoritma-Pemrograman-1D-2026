# kata = str(input("Masukkan Kata: ")).lower()

# hasil = kata == kata[::-1]
# if hasil:
#     print(f"Hasil Kata: {hasil} adalah palindrom")
# else:
#     print(f"Hasil Kata: {hasil} Tidak palindrom")

def palindrom(kata):
    kata = kata.lower()
    return kata == kata[::-1]

kata = str(input("Masukkan kata: "))
hasil = palindrom(kata)

if hasil:
    print(f'{hasil} kata adalah palindrom')
else:
    print(f'{hasil} kata bukan palindrom')
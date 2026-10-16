digit1 = int(input("Masukkan digit pertama: "))
digit2 = int(input("Masukkan digit kedua: "))
digit3 = int(input("Masukkan digit ketiga: "))

nilaip =digit1 * digit3
print("nilaip:", nilaip)
if digit2 % 2  == 0:
    nilaipbaru = nilaip - digit2
    print("pelacak awal:",nilaipbaru)
else:nilaipbaru =nilaip + 25
print("pelacak awal :",nilaipbaru)

if nilaip  % 3 == 0 :
    password = int(nilaipbaru / 3)
    print ("nilai kedua:", password)
          
else :
    password = int(nilaipbaru * 2)
print("nilai kedua:", password)

if password  > 50 :
    print("katagori: A")
elif password > 40 :
    print("katagori: B")

else :
    print("ditolak")


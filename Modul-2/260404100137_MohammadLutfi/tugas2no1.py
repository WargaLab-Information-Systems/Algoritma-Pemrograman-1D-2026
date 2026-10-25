pin=int(input("masukkan 3 digit angka:"))
digit1=pin // 100
digit2=(pin// 10)%10
digit3=pin%10
print("digit 1:",digit1)
print("digit 2:",digit2)
print("digit 3:",digit3)

nilaip= digit1 * digit3
print( nilaip)
if digit2 % 2 ==0:
    nilaipbaru=nilaip - digit2
    print("pelacak awal",nilaipbaru)
else:
    nilaipbaru = nilaip + 25
    print("pelacak awal",nilaipbaru)

if nilaip % 3==0:
    password=int (nilaipbaru / 3)
    print("nilai kedua",password)

else:
    password = int (nilaipbaru*3)
    print("nilai kedua",password)

if password > 50:
    print("kategori A")
elif password > 40:
    print("kategori b")
else:
    print("ditolak")


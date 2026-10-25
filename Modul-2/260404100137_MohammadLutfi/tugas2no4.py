pin=int(input("masukkan 3 digit angka:"))
jam=int(input("masukkan jam kedatangan:"))
digit1=pin // 100
digit2=(pin// 10)%10
digit3=pin%10
digit13= digit1 * digit3
print("digit 1:",digit1)
print("digit 2:",digit2)
print("digit 3:",digit3)
if pin % 5==0:
    print("mengevaluasi jam kedatangan:",jam)
    if jam <= 12:
        print("Garasi pagi terbuka")
    else:
        print("garasi malam terbuka,lampu dinyalakan akan muncul")
elif pin % 5==1:
    if digit13 == digit2:
        ("garasi vip terbuka khusus bos")
    else:
        print("kode genap ditolak,alarm berbunyi!")
else:
    print("akses ditolak sepenuhnya")


cctv="mode malam merekam" if jam > 18 else "mode siang standby"
print(cctv)





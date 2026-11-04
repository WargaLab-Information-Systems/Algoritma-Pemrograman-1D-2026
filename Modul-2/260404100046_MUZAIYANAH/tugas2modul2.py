totalBelanja = int(input("Total belanja Siti (dalam rupiah): "))
diskon = 0

if totalBelanja > 0:    
    if totalBelanja % 100000 == 0:
        gratis = True
    elif totalBelanja % 50000 == 0:
        gratis = False
        diskon = 50
    elif totalBelanja % 10000 == 0:
        gratis = False
        diskon = 20
    else:
        if totalBelanja >= 200000:
            gratis = False
            diskon = 10
        else:
            gratis = False

    if gratis == True:
        setelahDiskon = 0
    else:
        besarDiskon = int(totalBelanja) * (diskon / 100)
        setelahDiskon = int(totalBelanja) - besarDiskon
else:
    print("Siti tidak belanja apa apa")
    exit()


print("Total awal belanja sebelum diskon   : ", totalBelanja)


if gratis == False and diskon > 0:
    print("Diskon yang didapat              : ",  diskon, "%")

print("Total belanja setelah diskon        : ", int(setelahDiskon))

# poinKeanggotaan = "Poin Bertambah" if setelahDiskon > 0 else "Tidak Ada Poin"
# print("Status poin keanggotaan             : ", poinKeanggotaan)


if setelahDiskon > 0:
    print("Poin bertambah")
else:
    print("Tidak ada poin")
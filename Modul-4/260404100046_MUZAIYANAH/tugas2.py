gajiPokok = 100000
uangShiftMalam = 0
totalGaji = 0

for hari in range(1, 8):
    gajiHarian = 0
    upahLembur = 0
    
    jamLembur = int(input("Masukkan jam lembur: "))
    
    while jamLembur < 1 or jamLembur == 5 or jamLembur == 7:
        print("Format jam lembur tidak sesuai ketentuan.")
        jamLembur = int(input("Masukkan jam lembur: "))

    while True:
        shiftMalam = input("Apakah pekerja shift malam?(Y/N): ")
        if shiftMalam == "n" or shiftMalam == "N":
            shiftMlm = False
            break
        elif shiftMalam == "Y" or shiftMalam == "y":
            shiftMlm = True
            break
        else:
            print("Format tidak sesuai ketentuan!\nMasukkan ulang.")
            continue
            
    if jamLembur <= 3:
        upahLembur = 25000 * jamLembur
    elif jamLembur == 4:
        upahLembur = 100000
    elif jamLembur == 6:
        upahLembur = 200000
    elif jamLembur == 8:
        upahLembur = 300000
    elif jamLembur > 8:
        print("Pemberitahuan: jumlah lembur melebihi batas yang telah ditentukan.")
        upahLembur = 0
    
    gajiHarian = gajiPokok
    if shiftMlm == True:
        gajiHarian += 50000
    gajiHarian += upahLembur
    totalGaji += gajiHarian
    
    print("Total gaji hari ke-", hari, ": Rp", gajiHarian)
    
print("Total gaji dalam seminggu: Rp", totalGaji)
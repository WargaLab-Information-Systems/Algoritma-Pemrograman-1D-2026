gajiPokok = 100000
uangShiftMalam = 0
totalGaji = 0

for i in range(1, 8):
    gajiHarian = 0
    upahLembur = 0
    
    
    print("Hari pertama") if i == 1 else print(f"Hari ke-{i}")
    # if i == 1:
    #     print(f"--- Hari pertama")
    # else:
    #     print(f"--- Hari ke-{i}")

    jamLembur = int(input("Masukkan jam lembur: "))
    while jamLembur < 0 or jamLembur == 5 or jamLembur == 7:
        print("Format jam lembur tidak sesuai ketentuan.")
        jamLembur = int(input("Masukkan jam lembur: "))


    while True:
        shiftMalam = input("Apakah pekerja shift malam?(Y/N): ").lower
        if shiftMalam == "n":
            shiftMlm = False
            break
        elif shiftMalam == "Y" or shiftMalam == "y":
            shiftMlm = True
            break
        else:
            print("Format tidak sesuai ketentuan!\nMasukkan ulang.")
            continue
    print("-" * 30)
            
    if jamLembur <= 3:
        upahLembur = 25000 * jamLembur
    elif jamLembur == 4:
        upahLembur = 100000
    elif jamLembur == 6:
        upahLembur = 200000
    elif jamLembur == 8:
        upahLembur = 300000
    elif jamLembur > 8:
        print("Pemberitahuan: jumlah lembur melebihi batas yang ditentukan.")
        upahLembur = 0
    
    gajiHarian = gajiPokok
    if shiftMlm == True:
        gajiHarian += 50000
    gajiHarian += upahLembur
    totalGaji += gajiHarian
    
    if i == 1:
        print(f"Total gaji hari pertama: Rp{gajiHarian}")
    else:
        print(f"Total gaji hari ke-{i}: Rp{gajiHarian}")
    print("-" * 30)

print(f"Total gaji dalam seminggu: Rp{totalGaji}")
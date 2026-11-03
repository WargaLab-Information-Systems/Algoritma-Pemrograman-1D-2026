def palindrom(kata):
    balik = ""
    for huruf in kata:
        balik = huruf + balik
    return True if kata == balik else False


def main():
    while True:
        kata = str(input("Masukkan kata : (Input 0 untuk berhenti)"))
        if kata == "0":
            break
        print(f"{kata} adalah palindrom") if palindrom(kata) else print(f"{kata} bukan palindrom")
        print("-" * 20)
        
main()
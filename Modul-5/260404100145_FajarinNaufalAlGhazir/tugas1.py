def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    while True:
        n = int(input("Masukkan hari (input 0 atau negatif untuk berhenti): "))
        if n <= 0:
            break
        else:
            pass
        print(f"Pelanggan pada hari ke-{n} = {fibonacci(n)}")
        
main()
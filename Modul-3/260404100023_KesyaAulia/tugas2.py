n = int(input("berapa baris yang di perlukan: "))

while n <2 or n >15:
    n = int(input("berapa baris yang di perlukan: "))

for i in range (1, n + 1 ):
    print(" " * (n - i), end="")
    
    for j in range(1, i + 1):
        print(j % 10, end="")
    
    for j in range(i - 1, 0, -1):
        print(j % 10, end="")
    print()

for i in range (n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range (1, i + 1):
        print(j % 10, end="")
    for j in range (i - 1, 0, -1):
        print(j % 10, end="")
    print()

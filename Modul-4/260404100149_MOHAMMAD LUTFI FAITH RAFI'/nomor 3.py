n = int(input("Masukkan bilangan bulat positif: "))

while n <= 0:
    print("Bilangan harus lebih dari 0.")
    n = int(input("Masukkan bilangan bulat positif: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):  #untuk mencetak angka menaik di sebelah kiri 
        print(j, end=" ")

    for spasi in range(2 * (n - i) + 2): # untuk mengatur jarak antara kedua piramida
        print(" ", end=" ")

    for k in range(i, 0, -1):  # untuk mencetak angka menurun disebelah kanan (cermin)
        print(k, end=" ")

    print()

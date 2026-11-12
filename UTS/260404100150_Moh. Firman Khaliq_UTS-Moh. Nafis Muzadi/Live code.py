harga_tiket = {
    "regular": 40000,
    "vip": 75000,
    "vvip": 100000,
}

# INPUTAN UNTUK MEMBELI TIKET DAN MEMILIH JUMLAH TIKET
tiket_dibeli = input("Masukkan tiket yang dibeli: ").strip().lower()
if tiket_dibeli not in harga_tiket:
    print("Tiket tidak valid")
else:
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))
    member_card = input("Apakah anda punya member card (Ya/tidak): ").strip().lower()

    # PERHITUNGAN HARGA TIKET
    harga = harga_tiket[tiket_dibeli] * jumlah_tiket

    if tiket_dibeli == "regular":
        print("Anda bisa membeli minuman seharga 10000 Rupiah")
        minuman = input("Beli atau tidak (Y/N): ").strip().upper()
        if minuman == "Y":
            harga += 10000

    diskon = 0
    if jumlah_tiket > 3:
        if member_card == "ya":
            diskon = 0.15
        else:
            diskon = 0.10

    harga_total = harga * (1 - diskon)
    nominal = int(input("Masukkan jumlah uang: "))
    kembalian = nominal - harga_total

    print(f"Harga total: {harga_total:.0f} Rp.")
    if tiket_dibeli in ("vip", "vvip"):
        print("Anda mendapat minuman gratis")
    print(f"Nominal: {nominal} Rp.")
    print(f"Kembalian: {kembalian:.0f} Rp.")


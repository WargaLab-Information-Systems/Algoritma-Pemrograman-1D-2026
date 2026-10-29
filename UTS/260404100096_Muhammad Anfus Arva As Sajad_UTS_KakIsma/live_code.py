regular = 40000
vip = 75000
vvip = 100000
harga_minuman = 10000

ticket_reguler = 0
ticket_vip = 0
ticket_vvip = 0
minuman_bayar = 0   # jumlah minuman yang dibayar (khusus regular)

# --- PEMESANAN TIKET (diulang sampai user ketik 'cukup') ---
beli = input("Ticket apa yang ingin anda beli?? (regular/vip/vvip/ketik 'cukup' jika sudah): ").lower()
while beli != "cukup":

    if beli == "regular":
        ticket_reguler += 1
        tambahan = input("Apakah anda mau menambah minuman (Y/N): ")
        # validasi: ulangi terus sampai jawabannya Y/y/N/n
        while tambahan not in ("Y", "y", "N", "n"):
            tambahan = input("Masukkan hanya Y atau N: ")
        if tambahan == "Y" or tambahan == "y":
            minuman_bayar += 1
    elif beli == "vip":
        ticket_vip += 1
        print("Selamat! Anda mendapat minuman gratis")
    elif beli == "vvip":
        ticket_vvip += 1
        print("Selamat! Anda mendapat minuman gratis")
    else:
        print("masukkan ulang")

    # tanya lagi di dalam loop supaya perulangan bisa berhenti
    beli = input("Mau beli tiket lagi? (regular/vip/vvip/ketik 'cukup' jika sudah): ").lower()

# --- HITUNG TOTAL ---
total_tiket = ticket_reguler + ticket_vip + ticket_vvip

if total_tiket == 0:
    print("Anda belum membeli tiket apa pun")
    exit()

total = (ticket_reguler * regular) + (ticket_vip * vip) + (ticket_vvip * vvip) + (minuman_bayar * harga_minuman)
print("Total sebelum diskon:", total)

# --- DISKON (hanya kalau tiket lebih dari 3) ---
if total_tiket > 3:
    mbcard = input("Apakah Anda memiliki Member Card (Yes/No): ").lower()
    while mbcard != "yes" and mbcard != "no":
        mbcard = input("Masukkan hanya Yes atau No: ").lower()

    if mbcard == "yes":
        total = total * 85 // 100   # diskon 15%
    else:
        total = total * 90 // 100   # diskon 10%
    print("Total setelah diskon:", total)
else:
    print("Tiket 3 atau kurang, tidak ada diskon")

# --- PEMBAYARAN (diulang sampai uang cukup) ---
uang = 0
while uang < total:
    print("Sisa yang harus dibayar:", total - uang)
    bayar = input("masukkan uang untuk pembayaran: ")
    if bayar.isdigit() and int(bayar) > 0:
        uang += int(bayar)
    else:
        print("Input harus angka lebih dari 0")

kembalian = uang - total   # menghitung kembalian
print("Pembayaran berhasil")
print("Kembalian:", kembalian)
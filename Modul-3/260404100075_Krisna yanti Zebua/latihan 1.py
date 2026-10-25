TARIF_DASAR = 3000
BATAS_1 = 6     # km, batas tarif dasar
BATAS_2 = 15    # km, batas tarif bertingkat pertama
TARIF_KM_1 = 1000
TARIF_KM_2 = 500


def tarif_normal(jarak):
    """Hitung tarif tanpa diskon dengan menjumlahkan tiap bagian jarak."""
    km_tingkat_1 = min(max(jarak - BATAS_1, 0), BATAS_2 - BATAS_1)
    km_tingkat_2 = max(jarak - BATAS_2, 0)
    return TARIF_DASAR + km_tingkat_1 * TARIF_KM_1 + km_tingkat_2 * TARIF_KM_2


def rupiah(nilai):
    return "Rp" + f"{nilai:,}".replace(",", ".")


def minta_jarak():
    """Minta input sampai valid. Mengembalikan 0 (selesai) atau jarak positif."""
    while True:
        teks = input("Jarak (km, 0 = selesai): ").strip()
        try:
            jarak = int(teks)
        except ValueError:
            print("  Harus berupa bilangan bulat.")
            continue
        if jarak < 0:
            print("  Jarak negatif tidak valid, ulangi.")
            continue
        return jarak

5

def main():
    daftar_jarak = []
    pendapatan = 0

    print("=== Kasir Pak Budi - Terminal Bus Sidoarjo ===")

    while True:
        jarak = minta_jarak()
        if jarak == 0:
            break

        daftar_jarak.append(jarak)
        urutan = len(daftar_jarak)
        bayar = tarif_normal(jarak)

        if urutan % 5 == 0:
            bayar //= 2
            print(f"  Penumpang {urutan} ({jarak} km): {rupiah(bayar)} (diskon 50%)")
        else:
            print(f"  Penumpang {urutan} ({jarak} km): {rupiah(bayar)}")

        pendapatan += bayar

    print("\n--- Ringkasan ---")
    print("Jumlah penumpang :", len(daftar_jarak))
    print("Total pendapatan :", rupiah(pendapatan))

    if daftar_jarak:
        print("Jarak terjauh    :", max(daftar_jarak), "km")
        print(f"Rata-rata jarak  : {sum(daftar_jarak) / len(daftar_jarak):.2f} km")
    else:
        print("Jarak terjauh    : -")
        print("Rata-rata jarak  : -")


if __name__ == "__main__":
    main()
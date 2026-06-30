# Latihan 1
umur = 17

if umur >= 17:
    print("Selamat! Kamu sudah boleh membuat SIM.")
else: 
    print("Maaf. Kamu belum cukup umur.")

# Latihan 2
nilai = 100

if nilai >= 75:
    print("Selamat! Kamu dinyatakan LULUS 🎉")
else:
    print("Semangat! kamu BELUM lulus.")


# Latihan 3
nama_barang = input("Nama Barang     : ")
harga_barang = int(input("Harga Barang    : "))
jumlah_barang = int(input("Jumlah Barang   : "))

total = harga_barang * jumlah_barang

print("\n" + "=" * 35)
print("         STRUK PEMBELIAN")
print("=" * 35)

print(f"Nama Barang : {nama_barang}")
print(f"Harga       : Rp{harga_barang:,}")
print(f"Jumlah      : {jumlah_barang}")

print("-" * 35)

print(f"Total       : Rp{total:,}")

if total >= 100000:
    diskon = total * 0.10
    bayar = total - diskon

    print(f"Diskon (10%) : Rp{diskon:,.0f}")
    print("-" * 35)
    print(f"Total Bayar  : Rp{bayar:,.0f}")
    print("=" * 35)
    print("🎉 Selamat! Anda mendapatkan diskon 10%.")

else:
    print(f"Diskon       : Rp0")
    print("-" * 35)
    print(f"Total Bayar  : Rp{total:,}")
    print("=" * 35)
    print("Terima kasih telah berbelanja 😊")
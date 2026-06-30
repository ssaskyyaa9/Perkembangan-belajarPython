# Tugas 1
nilai = int(input("Masukan Nilai    : "))

print("\n" + "=" * 35)
print("       HASIL PENILAIAN")
print("=" * 35)

print(f"nilai : {nilai}")

if nilai >= 90:
    print("Grade: A 🏆")

elif nilai >= 80:
    print("Grade: B 😊")

elif nilai >= 70:
    print("Grade: C 🙂")

else:
    print("Grade: D 😢")

# Tugas 2
umur = int(input("Masukan Umur    : "))

print("\n" + "=" * 35)
print("       HASIL PENENTUAN")
print("=" * 35)

print(f"umur : {umur}")

if umur >= 60:
    print("Lansia 👴")

elif umur >= 18:
    print("Dewasa 👨")

elif umur >= 13:
    print("Remaja 🧑")

else:
    print("Anak-anak 👶")

# Tugas 3
username = input("Masukan Username  : ")
password = int(input("Masukan Password  : "))

isi_username = "admin"
isi_password = 12345

if username == isi_username and password == isi_password:
    print("login berhasil")

elif username != isi_username and password != isi_password:
    print("login gagal")

elif username != isi_username:
    print("username salah")

else:
    print("password salah")

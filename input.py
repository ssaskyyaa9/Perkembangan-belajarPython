# Latihan 1
Nama = input("Nama      : ")
Umur = int(input("Umur      : "))
Jurusan = input("Jurusan   : ")

print(f"Nama        : {Nama}")
print(f"Umur        : {Umur} Tahun")
print(f"Jurusan     : {Jurusan}")

print(f"Kamu pasti bisa {Nama}!")
print(f"SEMANGATTT {Nama}, belajar ini gaakan sia sia koo, kamu pasti bisa hebat kaya yang lain")

# Latihan 2
Nama = input("Masukan Nama          : ")
Tahun = int(input("Masukan Tahun Lahir   : "))
Umur = 2026 - Tahun

print(f"Nama    : {Nama}")
print(f"Umur mu sekarang adalah {Umur} tahun")

# Latihan 3
print(f"======================")
print(f"     Hasil Nilai      ")
print(f"======================")

Matematika = 90
Bahasa_Indonesia = 85
Bahasa_Inggris = 95

print(f"Matematika          : {Matematika}")
print(f"Bahasa Indonesia    : {Bahasa_Indonesia}")
print(f"Bahasa Inggris      : {Bahasa_Inggris}")

rata_rata =(Matematika + Bahasa_Indonesia + Bahasa_Inggris) / 3

print(f"rata-rata   : {rata_rata}")

# Latihan 4
nama = input("Masukan Nama Lengkap    : ")
kelas = (input("Masukan kelas           : "))
jurusan = input("Masukan Jurusan         : ")

print(f"yukk masukin nilai kamu untuk dihitung rata rata nya 🥰")

agama = int(input("Agama         : "))
pancasila = int(input("Pancasila     : "))
indonesia = int(input("Indonesia     : "))
pjok = int(input("PJOK          : "))
sejarah = int(input("Sejarah       : "))
matematika = int(input("Matematika    : "))
inggris = int(input("Inggris       : "))
koke = int(input("Koke          : "))
pkk = int(input("PKK           : "))
analisis = int(input("Analisis      : "))
jepang = int(input("Jepang        : "))
basis_data = int(input("Basis_data    : "))
pwd = int(input("PWD           : "))
pm = int(input("PM            : "))

nilai = [ agama, pancasila, indonesia, pjok, sejarah, matematika, inggris, koke, pkk, analisis, jepang, basis_data, pwd, pm ]

rata_rata = sum(nilai) / len(nilai)
tertinggi = max(nilai)
terendah = min(nilai)

print(f"======================")
print(f" Hasil Analisis Nilai ")
print(f"======================")

print(f"Nama    : {nama}")
print(f"Kelas   : {kelas}")
print(f"Jurusan : {jurusan}")

print(f"Nilai Rata rata : {rata_rata:.2f}")
print(f"Nilai Tertinggi : {tertinggi}")
print(f"Nilai Terendah  : {terendah}")